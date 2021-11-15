import logging


def fibonaci(input_list):
    next_entry = input_list[-2] + input_list[-1]
    input_list.append(next_entry)
    logging.info("This iteration is {}".format(input_list))
    if next_entry <= 100:
        fibonaci(input_list)
    else:
        logging.warning("This was the last iteration")


if __name__ == "__main__":
    logging.basicConfig(filename="example.log", filemode="w", level=logging.INFO)
    start_list = [0, 1]
    fibonaci(start_list)
