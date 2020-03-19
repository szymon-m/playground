#generator - >> yielding smth ->> creates iterator from range, string excerpt,, and mor
def create_tuple(t):
    for i in t.split(" "):
        yield int(i)


while True:
    user_input = input()

    input_string = "387 38 498 988 434 282 467 641 464 682 341 586 222 736 187 415 330 323 109 818 78 469 560 623 748 782 352 398 196 39 603 344 630 841 794 994 648 293 861 800 944 249 921 10 781 437 915 451 782 262"

    # input_string = input_string.replace(" ", "")

    t = create_tuple(input_string)

    r = tuple(t)

    print(type(r))

    print(r)


