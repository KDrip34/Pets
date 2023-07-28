pets = {
	'puppy': {
	'name':'phati',
	'owner':'chris',
		}, 
		'puppy': {
		'name': 'chance',
		'owner': 'Evan',
			},
			'puppy': {
			'name': 'Vic Dog',
			'owner': 'vic my barber',
				},
}	
for pets, pet_info in pets.items():
	print("\nType of Animal: " + pets)
	pet = pet_info['name'] + " " + pet_info['owner']
	print("\tName pet: " + pet.title())
