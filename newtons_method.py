  def f(x):
        return (x ** 2) - 1

    def df(x):
        return 2 * x

    try:
        solution_newton = newtons_method(f, df, initial_guess)
        fx_newton = f(solution_newton)

        print("x = {:.4f} | f(x) = {:.4f}".format(solution_newton, fx_newton))

    except ZeroDivisionError as error:
        print(str(error))


if __name__ == "__main__":
    main()


