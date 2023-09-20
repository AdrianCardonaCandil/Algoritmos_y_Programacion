def order_crossover(parent1, parent2, lower_bound, upper_bound):
    # Creo el array hijo con la misma longitud que los otros arrays.
    child1 = [0]*len(parent1)
    
    # Relleno el array hijo con los elementos del padre
    for elemento in range(lower_bound, upper_bound):
        child1[elemento] = parent1[elemento]
    
    # Relleno el array hijo con los elementos de la madre
    child_index = upper_bound
    mother_index = upper_bound
    
    while child_index % len(child1) != lower_bound:
        if parent2[mother_index % len(parent2)] not in child1:
            child1[child_index % len(child1)] = parent2[mother_index % len(parent2)]
            child_index += 1
        mother_index += 1
    
    return child1