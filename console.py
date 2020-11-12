import pdb

from models.city import City
from models.country import Country
from models.continent import Continent
from models.sight import Sight


import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.continent_repository as continent_repository
import repositories.sight_repository as sight_repository





# Continental regions Setup
continent_repository.delete_all()

continent1 = Continent('Europe')
continent_repository.save(continent1)
continent2 = Continent('Asia')
continent_repository.save(continent2)
continent3 = Continent('Africa')
continent_repository.save(continent3)
continent4 = Continent('North America')
continent_repository.save(continent4)
continent5 = Continent('South America')
continent_repository.save(continent5)
continent6 = Continent('Australia & Oceania')
continent_repository.save(continent6)


# Country Example Setup
country_repository.delete_all()

country1 = Country('Scotland', continent1, False)
country_repository.save(country1)


# City Example Setup
city_repository.delete_all()

city1 = City('Edinburgh', country1, False, "Seagulls everywhere!")
city_repository.save(city1)

city2 = City('Glasgow', country1, False, "Deepfried Mars Bar")
city_repository.save(city2)

pdb.set_trace()