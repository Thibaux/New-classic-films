import requests
from bs4 import BeautifulSoup

eye_classics = list();
eye_restored_unseen = list();
eye_premiers = list();

def EyeAllfilms():
	def EyeClassics():
		global eye_classics
		EyeFilmNames = list();
		EyeFilmDirectors = list();
		url = 'https://www.eyefilm.nl/en/themes/eye-classics#full-program'
		headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.11 Safari/537.36'}
		page = requests.get(url, headers = headers)
		soup = BeautifulSoup(page.content, 'html.parser')

		filmNames = soup.find_all('h4', {'class': 'h3 full-program-title'})
		FilmDirectors = soup.find_all('div', {'class': 'full-program-subtitle'})

		for filmName in filmNames:
			filmName = filmName.text
			EyeFilmNames.append(filmName)

		for FilmDirector in FilmDirectors:
			FilmDirector = FilmDirector.text
			EyeFilmDirectors.append(FilmDirector)

		arr_length = len(EyeFilmNames)
		for i in range(arr_length):
			eye_classics.extend([EyeFilmNames[i], EyeFilmDirectors[i]])

		eye_classics = '\n'.join(eye_classics)

	def EyeRestored_Unseen():
		global eye_restored_unseen
		EyeFilmNames = list();
		EyeFilmDirectors = list();
		url = 'https://www.eyefilm.nl/en/themes/restored-unseen#full-program'
		headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.11 Safari/537.36'}
		page = requests.get(url, headers = headers)
		soup = BeautifulSoup(page.content, 'html.parser')

		filmNames = soup.find_all('h4', {'class': 'h3 full-program-title'})
		FilmDirectors = soup.find_all('div', {'class': 'full-program-subtitle'})

		for filmName in filmNames:
			filmName = filmName.text
			EyeFilmNames.append(filmName)

		for FilmDirector in FilmDirectors:
			FilmDirector = FilmDirector.text
			EyeFilmDirectors.append(FilmDirector)

		arr_length = len(EyeFilmNames)
		for i in range(arr_length):
			eye_restored_unseen.extend([EyeFilmNames[i], EyeFilmDirectors[i]])

		eye_restored_unseen = '\n'.join(eye_restored_unseen)

	def EyePremiers():
		global eye_premiers
		EyeFilmNames = list();
		EyeFilmDirectors = list();
		url = 'https://www.eyefilm.nl/en/themes/premieres#full-program'
		headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.11 Safari/537.36'}
		page = requests.get(url, headers = headers)
		soup = BeautifulSoup(page.content, 'html.parser')

		filmNames = soup.find_all('h4', {'class': 'h3 full-program-title'})
		FilmDirectors = soup.find_all('div', {'class': 'full-program-subtitle'})

		for filmName in filmNames:
			filmName = filmName.text
			EyeFilmNames.append(filmName)

		for FilmDirector in FilmDirectors:
			FilmDirector = FilmDirector.text
			EyeFilmDirectors.append(FilmDirector)

		arr_length = len(EyeFilmNames)
		for i in range(arr_length):
			eye_premiers.extend([EyeFilmNames[i], EyeFilmDirectors[i]])

		eye_premiers = '\n'.join(eye_premiers)

	EyeClassics()
	EyeRestored_Unseen()
	EyePremiers()


def PrintConsole():
	EyeAllfilms()
	eye_all_films = f"""
			EYE

	Eye Classics

{eye_classics}

	Eye Restored & Unseen

{eye_restored_unseen}

	Eye Primiers

{eye_premiers}

	"""
	print(eye_all_films)
PrintConsole()
	