# data classes in Python automatically generate common methods with the @dataclass decorator (__init__, __repr__, __eq__, etc.)
# computed properties (like mass_to_flipper_length_ratio) can be defined
# using @property (like getter in TS)

from dataclasses import asdict, astuple, dataclass


@dataclass
class WeightEntry:
    species: str
    sex: str
    body_mass: int
    flipper_length: int

    @property
    def mass_to_flipper_length_ratio(self):
        return self.body_mass / self.flipper_length

    def set_mass_to_flipper_length_ratio(self, ratio: float):
        self.body_mass = int(self.flipper_length * ratio)


entry = WeightEntry("Adlie", "FEMALE", 3700, 185)
print(entry.mass_to_flipper_length_ratio)  # prints the current ratio

entry.set_mass_to_flipper_length_ratio(20.0)  # updates body_mass
print("After:", entry.mass_to_flipper_length_ratio)


# TS equivalent:
# class WeightEntry {
#   constructor(
#     public species: string,
#     public sex: string,
#     public body_mass: number,
#     public flipper_length: number
#   ) {}

#   get massToFlipperLengthRatio(): number {
#     return this.body_mass / this.flipper_length;
#   }

#   setMassToFlipperLengthRatio(ratio: number): void {
#     this.body_mass = this.flipper_length * ratio;
#   }
# }

# TS
# const entry = new WeightEntry('Adlie', 'FEMALE', 3700, 185);
# console.log(entry.massToFlipperLengthRatio);
# entry.setMassToFlipperLengthRatio(20)
# console.log('After:', entry.massToFlipperLengthRatio);


##################

weight_log = [
    ("Gentoo", "MALE", 5500.0, 210),
    ("Chinstrap", "MALE", 4300.0, 190),
    ("Adlie", "MALE", 3800.0, 180),
    ("Gentoo", "MALE", 5800.0, 220),
    ("Chinstrap", "MALE", 4100.0, 195),
    ("Adlie", "MALE", 3975.0, 185),
    ("Gentoo", "MALE", 5400.0, 215),
    ("Chinstrap", "MALE", 4800.0, 200),
    ("Chinstrap", "FEMALE", 3800.0, 190),
    ("Adlie", "FEMALE", 3450.0, 175),
    ("Chinstrap", "MALE", 3950.0, 190),
    ("Gentoo", "MALE", 5250.0, 215),
    ("Gentoo", "FEMALE", 4300.0, 195),
    ("Gentoo", "MALE", 4925.0, 205),
    ("Adlie", "FEMALE", 3550.0, 175),
    ("Adlie", "MALE", 3950.0, 185),
    ("Chinstrap", "MALE", 3800.0, 185),
    ("Chinstrap", "MALE", 4050.0, 190),
    ("Adlie", "MALE", 3650.0, 180),
    ("Adlie", "FEMALE", 3175.0, 170),
]


labeled_entries = []

for species, sex, body_mass, flipper_length in weight_log:
    labeled_entries.append(WeightEntry(species, sex, body_mass, flipper_length))

# Print a list of the first 5 mass_to_flipper_length_ratio values
print([entry.mass_to_flipper_length_ratio for entry in labeled_entries[:5]])
