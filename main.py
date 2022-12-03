from concurrent.futures import ThreadPoolExecutor
import logging
import threading
import time


class Barber:
    def __init__(self) -> None:
        self.active = False


class Customer:
    def __init__(self, name: int) -> None:
        self.name = name
        self.accommodated = False


class BarberShop:
    def __init__(self) -> None:
        self.barber = Barber()
        self.barber_chair = self.barber
        self.queue_seats = [None, None, None, None, None]
        self._lock = threading.Lock()
    
    def is_barber_free(self) -> bool:
        return self.barber_chair is None or isinstance(self.barber_chair, Barber)

    def open(self, name: int) -> None:
        logging.info("Thread %s: customer walks in", name)
        customer = Customer(name)

        if all(self.queue_seats):
            logging.info("Thread %s: customer leaves due to no space", name)
            return

        if self.is_barber_free():
            with self._lock:
                self.barber_chair = customer
                logging.info("Thread %s: barber shaves customer", name)
                time.sleep(0.1)
                self.barber_chair = None
                logging.info("Thread %s: customer leaves after shaving", name)
        else:
            with self._lock:
                seat_no = self.queue_seats.index(None)
                self.queue_seats[seat_no] = customer
                logging.info("Thread %s: customer waits in %s", name, seat_no)
                time.sleep(0.1)

            while self.queue_seats[seat_no] is not None:
                if self.is_barber_free():
                    with self._lock:
                        self.barber_chair = customer
                        logging.info("Thread %s: barber shaves customer", name)
                        time.sleep(0.1)
                        self.barber_chair = None
                        self.queue_seats[seat_no] = None
                        logging.info("Thread %s: customer leaves after shaving", name)
                with self._lock:
                    time.sleep(0.1)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    barber_shop = BarberShop()

    with ThreadPoolExecutor(max_workers=5) as executor:
        for index in range(100):
            executor.submit(barber_shop.open, index)
