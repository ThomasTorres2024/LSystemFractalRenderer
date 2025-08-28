class FileReader:
    fileName : str 
    lSysInfo : list[str,dict] = []

    def __init__(self,fileName,dd, iterations, turtle) :
        self.fileName = fileName
        print(self.fileName)
        try:
            with open(fileName) as file:
                line_count = sum(1 for line in file)
                file.seek(0)

                for i in range(line_count//6):
                    self.lSysInfo.append(self.go_through_file(file,dd,iterations,turtle))
        except FileNotFoundError:
            print("ERROR: File not found.")
            self.lSysInfo = []
    

    def get_all_LSys(self) -> list[str,dict]:
        return self.lSysInfo

    def go_through_file(self, file, dd, iterations, turtle):

        system_hash : dict = {"grapher" : turtle , "drawing_dist" : dd, "iterations" : iterations}
        system_hash["name"] = file.readline().strip()

        permutations = file.readline().split(":")
        permutations_dict : dict = {}

        for j in range(int(len(permutations)/2)):
            new_permu : list[str] = []
            permutations[j*2] = permutations[j*2].strip()
            permutations[j*2+1] = permutations[j*2+1].strip()
            for i in range(len(permutations[j*2+1])):
                new_permu+=permutations[j*2+1][i]
            permutations_dict[str(permutations[j*2])] = new_permu
        

        system_hash["permutations"] = permutations_dict
        axiom = file.readline().strip()
    
        axiomList = []
        for char in axiom:
            axiomList += char
        system_hash["axiom"] = axiomList 
        system_hash["angle"] = int(file.readline().strip())
        system_hash["items_run"] = int(file.readline().strip())
        system_hash["scaler"] = float(file.readline().strip())

        return system_hash