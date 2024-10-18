from TraceRecursio.tracer import Trace


@Trace
def reverse_string(string):
    if len(string) == 0:
        return ""

    return reverse_string(string[1:]) + string[0]


if __name__ == "__main__":
    print(reverse_string("ABC"))

    Trace.get_graph("reverse_string")
