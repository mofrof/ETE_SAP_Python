with open("C:\\Users\\Andréa\\Desktop\\Exemplo.txt", "r") as f:
    lines = f.readlines()
with open("C:\\Users\\Andréa\\Desktop\\Exemplo.txt", "w") as f:
    for line in lines:
        
        if line.startswith("54321") != True :
            print(line);
            f.write(line)