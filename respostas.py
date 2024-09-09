def exercicio1(vector: tuple) -> int|float:
    list_of_values = []
    for value in vector:
        try:
            if not isinstance(value, (int,float)):
                raise TypeError(f"One parameter of the vector is not a number: {value}")
        except TypeError as error:
            print(f"an error has occured: {error}")
            return
        else:
            list_of_values.append(value*value)
    squared_sum = sum(list_of_values)
    return round(squared_sum**(1/2), 3)

def exercicio2(p1: tuple, p2: tuple) -> tuple:
    try:
        if not (len(p1) == 2 or len(p2) == 2):
            raise Exception
        for value in p1:
            if not isinstance(value, (int,float)):
                raise ValueError
        for value in p2:
            if not isinstance(value, (int, float)):
                raise ValueError
        if p1[0] == p2[0]:
            raise ZeroDivisionError
    except (ZeroDivisionError, ValueError, Exception) as error:
        match error:
            case ZeroDivisionError():
                print("não é possível calcular o coeficiente angular")
            case ValueError():
                print("As coordenadas devem ser números")
            case Exception():
                print("As coordenadas devem ter apenas dois valores")
    else:
        angular_coef = (p2[1]-p1[1])/(p2[0]-p1[0])
        fre_coef = p1[1] - angular_coef*p1[0]
        return (angular_coef, fre_coef)


