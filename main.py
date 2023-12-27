from abc import ABC, abstractmethod


class EarthMovingMachinery(ABC):

    def __init__(self, brand, engine_number, chassis_number, rental_date, number_of_days, operator):
        self.brand = brand
        self.engine_number = engine_number
        self.chassis_number = chassis_number
        self.rental_date = rental_date
        self.number_of_days = number_of_days
        self.operator = operator

    def get_machinery_brand(self):
        return self.brand

    def get_chassis(self):
        return self.chassis_number

    def get_engine_num(self):
        return self.engine_number

    def get_date(self):
        return self.rental_date

    def get_number_of_days(self):
        return self.number_of_days

    def get_operator(self):
        return self.operator

    @abstractmethod
    def check_discount(self):
        pass

    @abstractmethod
    def calculate_discount(self):
        pass

    @abstractmethod
    def calculate_rental_fees(self):
        pass


from abc import ABC, abstractmethod


class EarthMovingMachinery(ABC):

    def __init__(self, brand, engine_number, chassis_number, rental_date, number_of_days, operator):
        self.brand = brand
        self.engine_number = engine_number
        self.chassis_number = chassis_number
        self.rental_date = rental_date
        self.number_of_days = number_of_days
        self.operator = operator

    def get_machinery_brand(self):
        return self.brand

    def get_chassis(self):
        return self.chassis_number

    def get_engine_num(self):
        return self.engine_number

    def get_date(self):
        return self.rental_date

    def get_number_of_days(self):
        return self.number_of_days

    def get_operator(self):
        return self.operator

    @abstractmethod
    def check_discount(self):
        pass

    @abstractmethod
    def calculate_discount(self):
        pass

    @abstractmethod
    def calculate_rental_fees(self):
        pass


class Excavator(EarthMovingMachinery):

    def __init__(self, brand, engine_number, chassis_number, rental_date, kilos, number_of_days, hours, operator):
        super().__init__(brand, engine_number, chassis_number, rental_date, number_of_days, operator)
        self.hours = hours
        self.kilos = kilos
        self.fee_per_hour = 250

    def get_hours(self):
        return self.hours

    def get_kilos(self):
        return self.kilos

    def check_discount(self):
        return self.get_number_of_days() > 5

    def calculate_discount(self):
        discount = 0
        if self.check_discount():
            discount = (10 / 100.0) * (self.get_number_of_days() * 4700)
        return discount

    def calculate_rental_fees(self):
        rental_fare = 0
        if self.check_discount():
            rental_fare = (self.get_number_of_days() * 4700) - self.calculate_discount()
        elif 0 < self.get_number_of_days() <= 5:
            rental_fare = self.get_number_of_days() * 4700
        else:
            rental_fare = self.fee_per_hour * self.hours
        return rental_fare


from abc import ABC, abstractmethod


class EarthMovingMachinery(ABC):

    def __init__(self, brand, engine_number, chassis_number, rental_date, number_of_days, operator):
        self.brand = brand
        self.engine_number = engine_number
        self.chassis_number = chassis_number
        self.rental_date = rental_date
        self.number_of_days = number_of_days
        self.operator = operator

    def get_machinery_brand(self):
        return self.brand

    def get_chassis(self):
        return self.chassis_number

    def get_engine_num(self):
        return self.engine_number

    def get_date(self):
        return self.rental_date

    def get_number_of_days(self):
        return self.number_of_days

    def get_operator(self):
        return self.operator

    @abstractmethod
    def check_discount(self):
        pass

    @abstractmethod
    def calculate_discount(self):
        pass

    @abstractmethod
    def calculate_rental_fees(self):
        pass


class Grader(EarthMovingMachinery):

    def __init__(self, brand, engine_number, chassis_number, rental_date, kilos, number_of_days, operator):
        super().__init__(brand, engine_number, chassis_number, rental_date, number_of_days, operator)
        self.kilos = kilos

    def get_kilos(self):
        return self.kilos

    def check_discount(self):
        return self.get_number_of_days() > 6

    def calculate_discount(self):
        discount = 0
        if self.check_discount():
            discount = (10 / 100.0) * (self.get_number_of_days() * 3700)
        return discount

    def calculate_rental_fees(self):
        rental_fare = 0
        if self.check_discount():
            rental_fare = (self.get_number_of_days() * 3700) - self.calculate_discount()
        else:
            rental_fare = self.get_number_of_days() * 3700
        return rental_fare


class Crane(EarthMovingMachinery, ABC):

    def __init__(self, brand, engine_number, chassis_number, rental_date, number_of_days, operator):
        super().__init__(brand, engine_number, chassis_number, rental_date, number_of_days, operator)

class MachineOperator:
    def __init__(self, operator_id, full_name, age):
        self.operator_id = operator_id
        self.full_name = full_name
        self.age = age

    def get_operator_id(self):
        return self.operator_id

    def get_full_name(self):
        return self.full_name

    def get_age(self):
        return self.age
class Static_Crane(Crane):
    def __init__(self, brN, enN, chN, rnD, nod, height, operator):
        super().__init__(brN, enN, chN, rnD, nod, operator)
        self.height = height

    def get_height(self):
        return self.height

    def check_discount(self):
        if self.get_number_of_days() > 5:
            return True
        return False

    def calculate_discount(self):
        if self.check_discount():
            return (10 / 100.0) * 13200
        return 0

    def calculate_rental_fees(self):
        rent_fee = 0
        if self.get_height() > 10 and self.check_discount():
            rent_fee = ((self.get_height() * self.get_number_of_days()) * 200) - self.calculate_discount()
        else:
            rent_fee = (self.get_height() * self.get_number_of_days()) * 150
        return rent_fee

class MobileCrane(Crane):

    def __init__(self, brand, engine_number, chassis_number, rental_date, kilos, number_of_days, operator):
        super().__init__(brand, engine_number, chassis_number, rental_date, number_of_days, operator)
        self.kilos = kilos

    def get_kilos(self):
        return self.kilos

    def check_discount(self):
        return self.get_number_of_days() > 3

    def calculate_discount(self):
        discount = 0
        if self.check_discount():
            discount = (15 / 100.0) * (self.get_number_of_days() * 7100)
        return discount

    def calculate_rental_fees(self):
        rental_fare = 0
        if self.check_discount():
            rental_fare = (self.get_number_of_days() * 7100) - self.calculate_discount()
        else:
            rental_fare = self.get_number_of_days() * 7100
        return rental_fare

    class StaticCrane(Crane):

        def __init__(self, brand, engine_number, chassis_number, rental_date, number_of_days, height, operator):
            super().__init__(brand, engine_number, chassis_number, rental_date, number_of_days, operator)
            self.height = height

        def get_height(self):
            return self.height

        def check_discount(self):
            return self.get_number_of_days() > 5

        def calculate_discount(self):
            if self.check_discount():
                return (10 / 100.0) * 13200
            return 0

        def calculate_rental_fees(self):
            rent_fee = 0
            if self.get_height() > 10 and self.check_discount():
                rent_fee = ((self.get_height() * self.get_number_of_days()) * 200) - self.calculate_discount()
            else:
                rent_fee = (self.get_height() * self.get_number_of_days()) * 150
            return rent_fee

        class Staff:
            def __init__(self, staff_first_name, staff_last_name, staff_id, salary):
                self.staff_first_name = staff_first_name
                self.staff_last_name = staff_last_name
                self.staff_id = staff_id
                self.salary = salary

            def get_staff_first_name(self):
                return self.staff_first_name

            def get_staff_last_name(self):
                return self.staff_last_name

            def get_staff_id(self):
                return self.staff_id

            def get_salary(self):
                return self.salary

            def get_full_name(self):
                return f"{self.staff_first_name} {self.staff_last_name}"

class Client:
    def __init__(self, client_number, client_first_name, client_last_name, client_address, client_contact_num):
        self.client_number = client_number
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self.client_address = client_address
        self.client_contact_num = client_contact_num

    def get_client_first_name(self):
        return self.client_first_name

    def get_client_last_name(self):
        return self.client_last_name

    def get_client_full_name(self):
        return f"{self.client_first_name} {self.client_last_name}"

    def get_client_contact(self):
        return self.client_contact_num

    def get_client_address(self):
        return self.client_address

    def get_client_contact_num(self):
        return self.client_contact_num

    def get_client_number(self):
        return self.client_number

class Receipt:
    def __init__(self, receipt_number, client_number, client_address, client_contact_num, brand_name, engine_num,
                 chasis_num, rental_date, number_of_days, kilos, staff_id, amount_paid, hours=None):
        self.receipt_number = receipt_number
        self.client_number = client_number
        self.client_address = client_address
        self.client_contact_num = client_contact_num
        self.brand_name = brand_name
        self.engine_num = engine_num
        self.chasis_num = chasis_num
        self.rental_date = rental_date
        self.number_of_days = number_of_days
        self.hours = hours
        self.kilos = kilos
        self.staff_id = staff_id
        self.amount_paid = amount_paid

    def get_amount_paid(self):
        return self.amount_paid

    def get_receipt_number(self):
        return self.receipt_number

    def get_staff_id(self):
        return self.staff_id

    def get_client_number(self):
        return self.client_number

    def __str__(self):
        return f"\nClient Receipt \n[Receipt Number: {self.receipt_number}, " \
               f"\nClient Number: {self.client_number}, \nClient Address: {self.client_address}, " \
               f"\nClient Contact Number: {self.client_contact_num}, \nBrand Name: {self.brand_name}, " \
               f"\nEngine Number: {self.engine_num}, \nChasis Number: {self.chasis_num}, " \
               f"\nRental Date: {self.rental_date} \nNumber of days: {self.number_of_days}, " \
               f"\nHours: {self.hours}, \nKilometres: {self.kilos}, \nAssisted by: {self.staff_id}, " \
               f"\nAmount Paid: ${self.amount_paid}]"

import random

class Octagon:
    def __init__(self):
        self.machineries = []
        self.employees = []
        self.customers = []
        self.operators = []
        self.receipts = []

    def add_rented_machinery(self, rented_machine):
        self.machineries.append(rented_machine)

    def add_staff(self, staff):
        self.employees.append(staff)

    def record_client(self, client):
        self.customers.append(client)

    def add_operator(self, operator):
        self.operators.append(operator)

    def create_receipt_from_machinery(self, client_number, machine_to_rent, staff):
        new_receipt = None
        for client in self.customers:
            if client.get_client_number().lower() == client_number.lower():
                receipt_id = (
                    str(client.get_client_first_name()[0])
                    + client.get_client_last_name()[0]
                    + staff.get_staff_id()
                    + client.get_client_contact_num()[3:6].replace(" ", "")
                )
                brand_name = machine_to_rent.get_machinery_brand()
                engine_num = machine_to_rent.get_engine_num()
                chasis_num = machine_to_rent.get_chassis()
                rental_date = machine_to_rent.get_date()
                number_of_days = machine_to_rent.get_number_of_days()
                hours, kilos = 0, 0

                if isinstance(machine_to_rent, Excavator):
                    hours = machine_to_rent.get_hours()
                    kilos = machine_to_rent.get_kilos()
                elif isinstance(machine_to_rent, Mobile_Crane):
                    kilos = machine_to_rent.get_kilos()
                elif isinstance(machine_to_rent, Grader):
                    kilos = machine_to_rent.get_kilos()

                new_receipt = Receipt(
                    receipt_id,
                    client_number,
                    client.get_client_address(),
                    client.get_client_contact_num(),
                    brand_name,
                    engine_num,
                    chasis_num,
                    rental_date,
                    number_of_days,
                    hours,
                    kilos,
                    staff.get_staff_id(),
                    machine_to_rent.calculate_rental_fees(),
                )
                break

        if new_receipt is None:
            raise Exception("Client not found on the system. Add the client as a new client first...!!!")

        return new_receipt

    def print_receipt(self, client_num, machine_to_rent, staff):
        new_receipt = None
        receipt_created = False

        for client in self.customers:
            if client.get_client_number().lower() == client_num:
                new_receipt = self.create_receipt_from_machinery(client_num, machine_to_rent, staff)
                self.receipts.append(new_receipt)
                receipt_created = True

            if receipt_created:
                break

        if not receipt_created:
            raise Exception("No receipt created, thus nothing to print...")

        return str(new_receipt)

    def receipt_exists(self, receipt_num):
        for receipt in self.receipts:
            if receipt.get_receipt_number().lower() == receipt_num.lower():
                return True
        return False

    def highly_paid_receipt(self):
        highly_paid = None
        most_paid = float("-inf")

        for receipt in self.receipts:
            if receipt.get_amount_paid() > most_paid:
                highly_paid = receipt
                most_paid = receipt.get_amount_paid()

        return highly_paid

    def staff_exist(self, firstname, ID):
        for emp in self.employees:
            if (
                emp.get_staff_first_name().lower() == firstname.lower()
                and emp.get_staff_id().lower() == ID.lower()
            ):
                return True
        return False

    def total_amount_of_money_for_rented_machinery(self):
        total = 0

        for machinery in self.machineries:
            total += machinery.calculate_rental_fees()

        return total

    def receipt_with_specific_amount(self, amount):
        receipt_needed = "Not found!!"

        for receipt in self.receipts:
            if receipt.get_amount_paid() == amount:
                receipt_needed = str(receipt)

        return receipt_needed

    def tallest_static_crane(self):
        tallest_crane = None
        tallest_metres = float("-inf")

        for earthmover in self.machineries:
            if isinstance(earthmover, Static_Crane):
                if earthmover.get_height() > tallest_metres:
                    tallest_metres = earthmover.get_height()
                    tallest_crane = earthmover

        return tallest_crane

    def how_many_day_specific_machine_rented(self, engine_num):
        num_days = 0

        for machinery in self.machineries:
            if machinery.get_engine_num().lower() == engine_num.lower():
                num_days = machinery.get_number_of_days()

        return num_days

    def get_staff_did_not_assist_client(self):
        assisting_staff_ids = {receipt.get_staff_id() for receipt in self.receipts}
        staff_without_clients = [staff for staff in self.employees if staff.get_staff_id() not in assisting_staff_ids]

        return staff_without_clients

    def get_clients_with_multiple_rentals(self):
        client_rental_counts = {}
        for receipt in self.receipts:
            client_num = receipt.get_client_number()
            client_rental_counts[client_num] = client_rental_counts.get(client_num, 0) + 1

        clients_with_multiple_rentals = [client for client, count in client_rental_counts.items() if count > 1]
        return clients_with_multiple_rentals

    def read_machinery_from_file(self, filename):
        machinery_list = []

        try:
            with open(filename, "r") as reader:
                for line in reader:
                    attributes = line.strip().split(",")
                    if len(attributes) == 9:
                        brand_name = attributes[0].strip()
                        engine_number = attributes[1].strip()
                        chasis_number = attributes[2].strip()
                        rental_date = attributes[3].strip()
                        km = int(attributes[4].strip())
                        number_of_days = int(attributes[5].strip())
                        operator_id = attributes[6].strip()
                        full_name = attributes[7].strip()
                        age = int(attributes[8].strip())

                        operator = MachineOperator(operator_id, full_name, age)
                        machinery = Mobile_Crane(brand_name, engine_number, chasis_number, rental_date, km, number_of_days, operator)
                        machinery_list.append(machinery)
                    else:
                        raise Exception("Invalid data format: " + line)
        except IOError as e:
            raise e

        return machinery_list

    def save_rented_machineries_info(self, my_file):
        with open(my_file, "a") as writer:
            for machinery in self.machineries:
                writer.write(str(machinery) + "\n\n")

    def read_rental_info_file(self, info_file):
        file_data = ""
        try:
            with open(info_file, "r") as file:
                file_data = file.read()
        except IOError as e:
            raise e

        return file_data

    def generate_parking_lot_entrance_or_exit_code(self, engine_no):
        rolling_code = ""
        random_numbers = random.randint(0, 9999)

        for machinery in self.machineries:
            if machinery.get_engine_num() == engine_no and not isinstance(machinery, Crane):
                some_length = len(machinery.get_chassis().replace(" ", ""))

                for i in range(some_length - 1, -1, -1):
                    rolling_code += machinery.get_chassis().upper()[i] + "*" + str(random_numbers)

        return rolling_code.replace(" ", "")


class OctagonApp:
    @staticmethod
    def main():
        octagon_rental_company = Octagon()

        oper1 = MachineOperator("OP001", "Michael De Vries", 29)
        oper2 = MachineOperator("OP002", "Setson Angala", 39)
        oper3 = MachineOperator("OP006", "Michael Paulus", 33)
        oper4 = MachineOperator("OP009", "John Smith", 35)
        oper5 = MachineOperator("OP011", "Jane Doe", 28)
        oper6 = MachineOperator("OP017", "Emily Johnson", 31)

        client1 = Client("LB001", "Lohan", "Beukes", "Otjomuise - Kitchen Street", "0610352541")
        client2 = Client("KN010", "Kelvin", "Nahum", "Dorlam - Fereira street", "0812547842")
        client3 = Client("JN201", "John", "Nangombe", "Black rock Street-Olympia", "0812978410")
        client4 = Client("JS410", "Jane", "Shimwe", "Sando Road", "0813696371")
        client5 = Client("EJ452", "Emily", "Jackson", "City Center- Circle 1", "0812505678")

        octagon_rental_company.record_client(client1)
        octagon_rental_company.record_client(client2)
        octagon_rental_company.record_client(client3)
        octagon_rental_company.record_client(client4)
        octagon_rental_company.record_client(client5)

        staff1 = Staff("Molina", "Diaz", "RC009", 20000.00)
        staff2 = Staff("Gracia", "Mendes", "RC088", 17000.00)
        staff3 = Staff("Robert", "Johnson", "RC017", 18500.00)
        staff4 = Staff("Amanda", "Smith", "RC025", 21000.00)
        staff5 = Staff("Lucas", "Williams", "RC034", 19500.00)

        octagon_rental_company.add_staff(staff1)
        octagon_rental_company.add_staff(staff2)
        octagon_rental_company.add_staff(staff3)
        octagon_rental_company.add_staff(staff4)
        octagon_rental_company.add_staff(staff5)

        machine1 = MobileCrane("HITACHI", "P033LKL", "MSJA099", "09-08-2022", 700000, 8, oper2)
        machine2 = Grader("KOMATSU", "EE093H", "D9DD760", "09-08-2022", 2000, 7, oper1)
        machine4 = Excavator("CATERPILLAR", "MMD609", "NE44KQ0", "09-08-2022", 76000, 0, 8, oper3)
        machine5 = Grader("VOLVO", "EE093K", "D9DD788", "09-08-2022", 5000, 6, oper1)
        crane1 = StaticCrane("GTI", "EPO8581", "CKL0120", "03-03-2022", 7, 15.0, oper4)
        crane2 = StaticCrane("FORD", "RTX2023", "LOE1474", "19-01-2023", 5, 20.0, oper5)
        machine6 = Excavator("JCB", "MMD667", "NE44KK0", "09-08-2022", 77000, 5, 0, oper2)
        machine7 = MobileCrane("SANY", "P033LQQ", "MSJA090", "08-08-2022", 7000, 4, oper3)
        crane3 = StaticCrane("KOMATSU", "EXT4102", "CHK0021", "07-07-2021", 3, 10.5, oper6)

        octagon_rental_company.add_rented_machinery(machine1)
        octagon_rental_company.add_rented_machinery(machine2)
        octagon_rental_company.add_rented_machinery(machine4)
        octagon_rental_company.add_rented_machinery(machine5)
        octagon_rental_company.add_rented_machinery(machine6)
        octagon_rental_company.add_rented_machinery(machine7)
        octagon_rental_company.add_rented_machinery(crane1)
        octagon_rental_company.add_rented_machinery(crane2)
        octagon_rental_company.add_rented_machinery(crane3)

        print("Does staff exist?:", octagon_rental_company.staff_exist("Gracia", "RC088"))
        print("Excavator fee is: $", machine4.calculate_rental_fees())

        try:
            print(octagon_rental_company.print_receipt("LB001", machine2, staff4))
        except Exception as e:
            print(str(e))

        try:
            print(octagon_rental_company.print_receipt(client2.get_client_number(), machine4, staff3))
        except Exception as e:
            print("An error occurred while printing the receipt..", str(e))

        try:
            print(octagon_rental_company.print_receipt(client5.get_client_number(), crane2, staff2))
        except Exception as e:
            print("An error occurred while printing the receipt..", str(e))

        try:
            print(octagon_rental_company.print_receipt(client2.get_client_number(), crane1, staff5))
        except Exception as e:
            print("An error occurred while printing the receipt..", str(e))

        try:
            print(octagon_rental_company.print_receipt(client5.get_client_number(), crane3, staff4))
        except Exception as e:
            print("An error occurred while printing the receipt..", str(e))

        print("\nHighly paid receipt:", octagon_rental_company.highly_paid_receipt().get_receipt_number())
        print("\nReceipt exists:", octagon_rental_company.receipt_exists("LBRC025035"))

        machines = []
        try:
            machines = octagon_rental_company.read_machinery_from_file("Cranes.txt")
        except Exception as e:
            print("An unexpected error occurred!!", str(e))

        print("\nFile machinery:")
        for mcn in machines:
            print(mcn.get_chassis())

        print("\nTallest Static crane:", octagon_rental_company.tallest_static_crane().get_engine_num())
        print("\nTotal amount of rented machine:", octagon_rental_company.total_amount_of_money_for_rented_machinery())
        print("\nReceipt with specific amount:", octagon_rental_company.receipt_with_specific_amount(4725.0))

        staff_without_clients = octagon_rental_company.get_staff_did_not_assist_client()
        print("\nStaff without clients:")
        for no_client in staff_without_clients:
            print(no_client.get_staff_id())

        bulk_renters = octagon_rental_company.get_clients_with_multiple_rentals()
        print("\nBulk renter clients:")
        for many_renter in bulk_renters:
            print(many_renter)

        print("\nRolling code:", octagon_rental_company.generate_parking_lot_entrance_or_exit_code("EE093H"))


# Run the application
OctagonApp.main()
