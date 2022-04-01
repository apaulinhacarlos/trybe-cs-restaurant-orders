class TrackOrders:
    def __init__(self):
        self.orders = []

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        return self.orders.append(
            {"customer": customer, "order": order, "day": day}
        )

    def get_most_ordered_dish_per_customer(self, customer):
        list_of_dishes = []
        for request in self.orders:
            if request["customer"] == customer:
                list_of_dishes.append(request["order"])
        result = max(set(list_of_dishes), key=list_of_dishes.count)
        return result

    def get_never_ordered_per_customer(self, customer):
        list_of_dishes = []
        list_of_dishes_per_customers = []

        for request in self.orders:
            list_of_dishes.append(request["order"])

        for request in self.orders:
            if request["customer"] == customer:
                list_of_dishes_per_customers.append(request["order"])

        result = set(list_of_dishes).difference(list_of_dishes_per_customers)
        return result

    def get_days_never_visited_per_customer(self, customer):
        list_of_days = []
        days_the_customer_went = []

        for request in self.orders:
            list_of_days.append(request["day"])

        for request in self.orders:
            if request["customer"] == customer:
                days_the_customer_went.append(request["day"])

        result = set(list_of_days).difference(days_the_customer_went)
        return result

    def get_busiest_day(self):
        list_of_days = []
        for request in self.orders:
            list_of_days.append(request["day"])
        result = max(set(list_of_days), key=list_of_days.count)
        return result

    def get_least_busy_day(self):
        list_of_days = []
        for request in self.orders:
            list_of_days.append(request["day"])
        result = min(set(list_of_days), key=list_of_days.count)
        return result
