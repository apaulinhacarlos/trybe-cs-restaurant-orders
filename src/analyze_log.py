import csv


def most_requested_dish_per_customer(customer, file):
    list_of_dishes = []
    for request in file:
        if request[0] == customer:
            list_of_dishes.append(request[1])
    result = max(set(list_of_dishes), key=list_of_dishes.count)
    return result


def number_of_dishes_requested_per_customer(customer, dish, file):
    list_of_dishes = []
    for request in file:
        if request[0] == customer:
            list_of_dishes.append(request[1])
    result = str(list_of_dishes.count(dish))
    return result


def dishes_never_requested_per_customer(customer, file):
    list_of_dishes = []
    list_of_dishes_per_customers = []

    for request in file:
        list_of_dishes.append(request[1])

    for request in file:
        if request[0] == customer:
            list_of_dishes_per_customers.append(request[1])

    result = set(list_of_dishes).difference(list_of_dishes_per_customers)
    return result


def days_never_went_to_the_restaurant_per_customer(customer, file):
    list_of_days = []
    days_the_customer_went = []

    for request in file:
        list_of_days.append(request[2])

    for request in file:
        if request[0] == customer:
            days_the_customer_went.append(request[2])

    result = set(list_of_days).difference(days_the_customer_went)
    return result


def reading_csv(path):
    with open(path, "r") as file:
        result = list(csv.reader(file))
    return result


def writing_txt(path, data):
    with open(path, "w") as file:
        file.write(data)
    pass


def analyze_log(path_to_file):
    if (path_to_file.endswith(".csv")) is False:
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")

    try:
        file = reading_csv(path_to_file)

        most_requested_dish_by_maria = most_requested_dish_per_customer(
            "maria", file
        )
        number_of_times_arnaldo_requested_hamburger = (
            number_of_dishes_requested_per_customer(
                "arnaldo", "hamburguer", file
            )
        )
        dishes_that_joao_never_requested = dishes_never_requested_per_customer(
            "joao", file
        )
        days_that_joao_did_not_go_to_the_restaurant = (
            days_never_went_to_the_restaurant_per_customer("joao", file)
        )

        writing_txt(
            "./data/mkt_campaign.txt",
            f"{most_requested_dish_by_maria}\n"
            f"{number_of_times_arnaldo_requested_hamburger}\n"
            f"{dishes_that_joao_never_requested}\n"
            f"{days_that_joao_did_not_go_to_the_restaurant}\n",
        )

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")


# Qual o prato mais pedido por 'maria'?
# Quantas vezes 'arnaldo' pediu 'hamburguer'?
# Quais pratos 'joao' nunca pediu?
# Quais dias 'joao' nunca foi na lanchonete?

# print(analyze_log("./data/orders_1.csv"))

# hamburguer
# 1
# {'pizza', 'coxinha', 'misto-quente'}
# {'sabado', 'segunda-feira'}
