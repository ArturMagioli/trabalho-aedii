import time

def major_choice(vet, begin, finish):
    start_time = time.time()  # início da cronometragem da parte                    #Θ(1)

    # Caso base
    if begin == finish:                                                             #Θ(1)
        end_time = time.time()                                                      #Θ(1)
        print(f"Tempo [{begin}:{finish}]: {end_time - start_time:.6f}s (base)")     #Θ(1)
        return vet[begin]                                                           #Θ(1)

    if begin < finish:                                                              #Θ(1)
        mid = (finish + begin) // 2                                                 #Θ(1)

        left = major_choice(vet, begin, mid)                                        #T(n/2)
        right = major_choice(vet, mid + 1, finish)                                  #T(n/2)

        if left == right:                                                           #Θ(1)
            end_time = time.time()                                                  #Θ(1)
            print(f"Tempo [{begin}:{finish}]: {end_time - start_time:.6f}s (mesmo candidato: {left})")  #Θ(1)
            return left                                                             #Θ(1)

        count_right = 0                                                             #Θ(1)
        count_left = 0                                                              #Θ(1)
        for i in range(begin, finish + 1):                                          #Θ(n)
            if vet[i] == left:                                                      #Θ(1)
                count_left += 1                                                     #Θ(1)
        for i in range(begin, finish + 1):                                          #Θ(n)
            if vet[i] == right:                                                     #Θ(1)
                count_right += 1                                                    #Θ(1)

        end_time = time.time()                                                      #Θ(1)
        print(f"Tempo [{begin}:{finish}]: {end_time - start_time:.6f}s (left: {count_left}, right: {count_right})") #Θ(1)

        if count_left > (finish - begin + 1) // 2:                                  #Θ(1)
            return left                                                             #Θ(1)
        elif count_right > (finish - begin + 1) // 2:                               #Θ(1)
            return right                                                            #Θ(1)
        else:                                                                       #Θ(0)
            return None                                                             #Θ(1)
                                                                                    #T(n)=2T(n/2)+n
#teste
vetor1= [5,6,8,9,2]
vetor2 = [2, 8, 7, 2, 2, 5, 2, 3, 2, 2]
vetor3= [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 3, 4, 2, 9, 5, 8, 1, 6, 10, 12, 0, 14]
print(f"\nEntrada: {vetor1}")
start_total = time.time()
result = major_choice(vetor1, 0, len(vetor1)-1)
end_total = time.time()
print(f"\nResultado final: {result}")
print(f"Tempo total de execução: {end_total - start_total:.6f}s")
print(f"\nEntrada: {vetor2}")
start_total = time.time()
result = major_choice(vetor2, 0, len(vetor2)-1)
end_total = time.time()
print(f"\nResultado final: {result}")
print(f"Tempo total de execução: {end_total - start_total:.6f}s")
print(f"\nEntrada: {vetor3}")
start_total = time.time()
result = major_choice(vetor3, 0, len(vetor3)-1)
end_total = time.time()
print(f"\nResultado final: {result}")
print(f"Tempo total de execução: {end_total - start_total:.6f}s")