class Myclass:
    def __init__(self, name, age) -> None:
        self.his_name = name
        self.his_age = age
        
    def __str__(self) -> str:
        return f"{self.his_name} {self.his_age}"
        
    
instance_one = Myclass("John", 30)
instance_two = Myclass("Janvier", 60)

print(instance_one)