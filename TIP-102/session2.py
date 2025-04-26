def most_endangered(species_list):
    lowest_population = species_list[0]["population"]
    endangered_species = species_list[0]["name"]

    for species in species_list:
        if species["population"] < lowest_population:
            lowest_population = species["population"]
            endangered_species = species["name"]

    return endangered_species
species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))
