import csv

movies_data = [
    {
        "title": "Inception",
        "genres": "Sci-Fi, Action, Thriller",
        "overview": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O., but his tragic past may doom the project.",
        "vote_average": 8.8,
        "release_date": "2010-07-16",
        "poster_url": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?q=80&w=400"
    },
    {
        "title": "The Dark Knight",
        "genres": "Action, Crime, Drama, Thriller",
        "overview": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
        "vote_average": 9.0,
        "release_date": "2008-07-18",
        "poster_url": "https://images.unsplash.com/photo-1518837695005-2083093ee35b?q=80&w=400"
    },
    {
        "title": "Interstellar",
        "genres": "Sci-Fi, Drama, Adventure",
        "overview": "When Earth becomes uninhabitable, a team of explorers undertakes the most important mission in human history: traveling beyond this galaxy to discover whether mankind has a future among the stars.",
        "vote_average": 8.7,
        "release_date": "2014-11-07",
        "poster_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=400"
    },
    {
        "title": "The Matrix",
        "genres": "Sci-Fi, Action",
        "overview": "When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the shocking truth--the life he knows is the elaborate deception of an evil cyber-intelligence.",
        "vote_average": 8.7,
        "release_date": "1999-03-31",
        "poster_url": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=400"
    },
    {
        "title": "Avatar",
        "genres": "Sci-Fi, Action, Adventure, Fantasy",
        "overview": "A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
        "vote_average": 7.9,
        "release_date": "2009-12-18",
        "poster_url": "https://images.unsplash.com/photo-1502082553048-f009c37129b9?q=80&w=400"
    },
    {
        "title": "The Avengers",
        "genres": "Action, Sci-Fi, Adventure",
        "overview": "Earth's mightiest heroes must come together and learn to fight as a team if they are to stop the mischievous Loki and his alien army from enslaving humanity.",
        "vote_average": 8.0,
        "release_date": "2012-05-04",
        "poster_url": "https://images.unsplash.com/photo-1569003339405-ea396a5a8a90?q=80&w=400"
    },
    {
        "title": "Titanic",
        "genres": "Romance, Drama",
        "overview": "A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.",
        "vote_average": 7.9,
        "release_date": "1997-12-19",
        "poster_url": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?q=80&w=400"
    },
    {
        "title": "La La Land",
        "genres": "Romance, Comedy, Drama, Music",
        "overview": "While navigating their careers in Los Angeles, a pianist and an actress fall in love while attempting to reconcile their aspirations for the future.",
        "vote_average": 8.0,
        "release_date": "2016-12-09",
        "poster_url": "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?q=80&w=400"
    },
    {
        "title": "The Notebook",
        "genres": "Romance, Drama",
        "overview": "A poor and passionate young man falls in love with a rich young woman, giving her a sense of freedom, but they are soon separated because of their social differences.",
        "vote_average": 7.8,
        "release_date": "2004-06-25",
        "poster_url": "https://images.unsplash.com/photo-1518199266791-5375a83190b7?q=80&w=400"
    },
    {
        "title": "Pulp Fiction",
        "genres": "Crime, Thriller, Drama",
        "overview": "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
        "vote_average": 8.9,
        "release_date": "1994-10-14",
        "poster_url": "https://images.unsplash.com/photo-1594909122845-11baa439b7bf?q=80&w=400"
    },
    {
        "title": "The Godfather",
        "genres": "Crime, Drama",
        "overview": "The aging patriarch of an organized crime dynasty in postwar New York City transfers control of his clandestine empire to his reluctant youngest son.",
        "vote_average": 9.2,
        "release_date": "1972-03-24",
        "poster_url": "https://images.unsplash.com/photo-1533928298208-27ff66555d8d?q=80&w=400"
    },
    {
        "title": "Forrest Gump",
        "genres": "Drama, Romance, Comedy",
        "overview": "The history of the United States from the 1950s to the '70s unfolds from the perspective of an Alabama man with an IQ of 75, who yearns to be reunited with his childhood sweetheart.",
        "vote_average": 8.8,
        "release_date": "1994-07-06",
        "poster_url": "https://images.unsplash.com/photo-1448375240586-882707db888b?q=80&w=400"
    },
    {
        "title": "The Shawshank Redemption",
        "genres": "Drama",
        "overview": "Over the course of several years, two convicts form a friendship, seeking consolation and, eventually, redemption through basic compassion.",
        "vote_average": 9.3,
        "release_date": "1994-09-23",
        "poster_url": "https://images.unsplash.com/photo-1473163928189-364b2c4e1135?q=80&w=400"
    },
    {
        "title": "Fight Club",
        "genres": "Drama, Thriller",
        "overview": "An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into much more.",
        "vote_average": 8.8,
        "release_date": "1999-10-15",
        "poster_url": "https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?q=80&w=400"
    },
    {
        "title": "Spirited Away",
        "genres": "Animation, Fantasy, Family",
        "overview": "During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beasts.",
        "vote_average": 8.6,
        "release_date": "2001-07-20",
        "poster_url": "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?q=80&w=400"
    },
    {
        "title": "Toy Story",
        "genres": "Animation, Comedy, Family",
        "overview": "A cowboy doll is profoundly threatened and jealous when a new spaceman action figure supplants him as top toy in a boy's bedroom.",
        "vote_average": 8.3,
        "release_date": "1995-11-22",
        "poster_url": "https://images.unsplash.com/photo-1558060370-d644479cb6f7?q=80&w=400"
    },
    {
        "title": "Finding Nemo",
        "genres": "Animation, Adventure, Family",
        "overview": "After his son is captured in the Great Barrier Reef and taken to Sydney, a timid clownfish embarks on a journey to bring him home.",
        "vote_average": 8.2,
        "release_date": "2003-05-30",
        "poster_url": "https://images.unsplash.com/photo-1546026423-cc4642628d2b?q=80&w=400"
    },
    {
        "title": "The Lion King",
        "genres": "Animation, Drama, Family",
        "overview": "A young lion prince is cast out of his pride by his cruel uncle, who claims he killed his father. While the uncle rules with an iron paw, the prince grows up beyond the Savannah, living by a philosophy of no worries.",
        "vote_average": 8.5,
        "release_date": "1994-06-24",
        "poster_url": "https://images.unsplash.com/photo-1516426122078-c23e76319801?q=80&w=400"
    },
    {
        "title": "Gladiator",
        "genres": "Action, Drama, History",
        "overview": "A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.",
        "vote_average": 8.5,
        "release_date": "2000-05-05",
        "poster_url": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?q=80&w=400"
    },
    {
        "title": "Jurassic Park",
        "genres": "Adventure, Sci-Fi, Thriller",
        "overview": "A pragmatic paleontologist visiting an almost complete theme park on an island in Central America is tasked with protecting a couple of kids after a power failure causes the park's cloned dinosaurs to run loose.",
        "vote_average": 8.2,
        "release_date": "1993-06-11",
        "poster_url": "https://images.unsplash.com/photo-1535083783855-76ae62b2914e?q=80&w=400"
    },
    {
        "title": "Star Wars: A New Hope",
        "genres": "Sci-Fi, Adventure, Action, Fantasy",
        "overview": "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids to save the galaxy from the Empire's world-destroying battle station, while also attempting to rescue Princess Leia from the mysterious Darth Vader.",
        "vote_average": 8.6,
        "release_date": "1977-05-25",
        "poster_url": "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=400"
    },
    {
        "title": "The Lord of the Rings: The Fellowship of the Ring",
        "genres": "Fantasy, Adventure, Action",
        "overview": "A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.",
        "vote_average": 8.8,
        "release_date": "2001-12-19",
        "poster_url": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=400"
    },
    {
        "title": "The Lord of the Rings: The Two Towers",
        "genres": "Fantasy, Adventure, Action",
        "overview": "While Frodo and Sam edge closer to Mordor with the help of the shifty Gollum, the divided fellowship makes a stand against Sauron's new ally, Saruman, and his hordes of Isengard.",
        "vote_average": 8.8,
        "release_date": "2002-12-18",
        "poster_url": "https://images.unsplash.com/photo-1524396309943-e03f5db0db87?q=80&w=400"
    },
    {
        "title": "The Lord of the Rings: The Return of the King",
        "genres": "Fantasy, Adventure, Action",
        "overview": "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.",
        "vote_average": 9.0,
        "release_date": "2003-12-17",
        "poster_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=400"
    },
    {
        "title": "Harry Potter and the Sorcerer's Stone",
        "genres": "Fantasy, Adventure, Family",
        "overview": "An orphaned boy enrolls in a school of wizardry, where he learns the truth about himself, his family and the terrible evil that haunts the magical world.",
        "vote_average": 7.6,
        "release_date": "2001-11-16",
        "poster_url": "https://images.unsplash.com/photo-1507504038482-7621c37b2f1d?q=80&w=400"
    },
    {
        "title": "Harry Potter and the Prisoner of Azkaban",
        "genres": "Fantasy, Adventure, Family",
        "overview": "Harry Potter, Ron and Hermione return to Hogwarts School of Witchcraft and Wizardry for their third year of study, where they delve into the mystery surrounding an escaped prisoner who poses a dangerous threat to the young wizard.",
        "vote_average": 7.9,
        "release_date": "2004-06-04",
        "poster_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=400"
    },
    {
        "title": "The Silence of the Lambs",
        "genres": "Thriller, Horror, Crime",
        "overview": "A top FBI cadet must receive the help of an incarcerated and manipulative cannibal killer to help catch another serial killer, a madman who skins his victims.",
        "vote_average": 8.6,
        "release_date": "1991-02-14",
        "poster_url": "https://images.unsplash.com/photo-1509248961158-e54f6934749c?q=80&w=400"
    },
    {
        "title": "The Conjuring",
        "genres": "Horror, Thriller, Mystery",
        "overview": "Paranormal investigators Ed and Lorraine Warren work to help a family terrorized by a dark presence in their farmhouse.",
        "vote_average": 7.5,
        "release_date": "2013-07-19",
        "poster_url": "https://images.unsplash.com/photo-1505635330303-3195302cf604?q=80&w=400"
    },
    {
        "title": "Get Out",
        "genres": "Horror, Thriller, Mystery",
        "overview": "A young African-American visits his white girlfriend's parents for the weekend, where his simmering uneasiness about their reception eventually reaches a boiling point.",
        "vote_average": 7.7,
        "release_date": "2017-02-24",
        "poster_url": "https://images.unsplash.com/photo-1534447677768-be436bb09401?q=80&w=400"
    },
    {
        "title": "A Quiet Place",
        "genres": "Horror, Sci-Fi, Thriller",
        "overview": "A family struggles for survival in a world where most humans have been killed by blind but noise-sensitive creatures. They are forced to communicate only in sign language to keep the creatures at bay.",
        "vote_average": 7.5,
        "release_date": "2018-04-06",
        "poster_url": "https://images.unsplash.com/photo-1448375240586-882707db888b?q=80&w=400"
    },
    {
        "title": "Eternal Sunshine of the Spotless Mind",
        "genres": "Romance, Sci-Fi, Drama",
        "overview": "When their relationship turns sour, a couple undergoes a medical procedure to have each other erased from their memories.",
        "vote_average": 8.3,
        "release_date": "2004-03-19",
        "poster_url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=400"
    },
    {
        "title": "Whiplash",
        "genres": "Drama, Music",
        "overview": "A promising young drummer enrolls at a cut-throat music conservatory where his dreams of greatness are mentored by an instructor who will stop at nothing to realize a student's potential.",
        "vote_average": 8.5,
        "release_date": "2014-10-10",
        "poster_url": "https://images.unsplash.com/photo-1511192336575-5a79af67a629?q=80&w=400"
    },
    {
        "title": "The Wolf of Wall Street",
        "genres": "Comedy, Drama, Biography",
        "overview": "Based on the true story of Jordan Belfort, from his rise to a wealthy stockbroker living the high life to his fall involving crime, corruption and the federal government.",
        "vote_average": 8.2,
        "release_date": "2013-12-25",
        "poster_url": "https://images.unsplash.com/photo-1502920514313-52581002a659?q=80&w=400"
    },
    {
        "title": "Superbad",
        "genres": "Comedy",
        "overview": "Two co-dependent high school seniors are forced to deal with separation anxiety after their plan to stage a booze-fueled party goes awry.",
        "vote_average": 7.6,
        "release_date": "2007-08-17",
        "poster_url": "https://images.unsplash.com/photo-1492684223066-81342ee5ff30?q=80&w=400"
    },
    {
        "title": "The Hangover",
        "genres": "Comedy",
        "overview": "Three buddies wake up from a bachelor party in Las Vegas, with no memory of the previous night and the bachelor missing. They make their way around the city in order to find their friend before his wedding.",
        "vote_average": 7.7,
        "release_date": "2009-06-05",
        "poster_url": "https://images.unsplash.com/photo-1522083165195-342750297f46?q=80&w=400"
    },
    {
        "title": "Shutter Island",
        "genres": "Thriller, Mystery, Drama",
        "overview": "In 1954, a U.S. Marshal investigates the disappearance of a murderer who escaped from a hospital for the criminally insane on Shutter Island, only to uncover a web of deception.",
        "vote_average": 8.2,
        "release_date": "2010-02-19",
        "poster_url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=400"
    },
    {
        "title": "Django Unchained",
        "genres": "Western, Action, Drama",
        "overview": "With the help of a German bounty hunter, a freed slave sets out to rescue his wife from a brutal Mississippi plantation owner.",
        "vote_average": 8.4,
        "release_date": "2012-12-25",
        "poster_url": "https://images.unsplash.com/photo-1509316975850-ff9c5edd0cd9?q=80&w=400"
    },
    {
        "title": "Inglourious Basterds",
        "genres": "War, Action, Drama",
        "overview": "In Nazi-occupied France during World War II, a plan to assassinate Nazi leaders by a group of Jewish U.S. soldiers coincides with a theatre owner's vengeful plans for the same.",
        "vote_average": 8.3,
        "release_date": "2009-08-21",
        "poster_url": "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?q=80&w=400"
    },
    {
        "title": "Parasite",
        "genres": "Thriller, Drama, Comedy",
        "overview": "Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.",
        "vote_average": 8.6,
        "release_date": "2019-05-30",
        "poster_url": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=400"
    },
    {
        "title": "Spider-Man: Into the Spider-Verse",
        "genres": "Animation, Action, Sci-Fi, Adventure",
        "overview": "Teen Miles Morales becomes the Spider-Man of his universe, and must join with five spider-powered individuals from other dimensions to stop a threat for all realities.",
        "vote_average": 8.4,
        "release_date": "2018-12-14",
        "poster_url": "https://images.unsplash.com/photo-1514565131-fce0801e5785?q=80&w=400"
    },
    {
        "title": "Back to the Future",
        "genres": "Sci-Fi, Comedy, Adventure",
        "overview": "Marty McFly, a 17-year-old high school student, is accidentally sent thirty years into the past in a time-traveling DeLorean invented by his close friend, the maverick scientist Doc Brown.",
        "vote_average": 8.5,
        "release_date": "1985-07-03",
        "poster_url": "https://images.unsplash.com/photo-1525609004556-c46c7d6cf0a3?q=80&w=400"
    },
    {
        "title": "Blade Runner 2049",
        "genres": "Sci-Fi, Thriller, Mystery",
        "overview": "A new blade runner, LAPD Officer K, unearths a long-buried secret that has the potential to plunge what's left of society into chaos. K's discovery leads him on a quest to find Rick Deckard, a former LAPD blade runner who has been missing for thirty years.",
        "vote_average": 8.0,
        "release_date": "2017-10-06",
        "poster_url": "https://images.unsplash.com/photo-1515621061946-eff1c2a352bd?q=80&w=400"
    },
    {
        "title": "Prisoners",
        "genres": "Thriller, Mystery, Drama",
        "overview": "When Keller Dover's daughter and her friend go missing, he takes matters into his own hands as the police pursue multiple leads and the pressure mounts.",
        "vote_average": 8.1,
        "release_date": "2013-09-20",
        "poster_url": "https://images.unsplash.com/photo-1515694346937-94d85e41e6f0?q=80&w=400"
    },
    {
        "title": "Gone Girl",
        "genres": "Thriller, Mystery, Drama",
        "overview": "With his wife's disappearance having become the focus of an intense media circus, a man sees the spotlight turned on him when it's suspected that he may not be innocent.",
        "vote_average": 8.1,
        "release_date": "2014-10-03",
        "poster_url": "https://images.unsplash.com/photo-1469474968028-56623f02e42e?q=80&w=400"
    },
    {
        "title": "The Grand Budapest Hotel",
        "genres": "Comedy, Drama",
        "overview": "A writer relates his adventures at a renowned European resort between the first and second World Wars with a concierge who is wrongly framed for murder.",
        "vote_average": 8.1,
        "release_date": "2014-03-28",
        "poster_url": "https://images.unsplash.com/photo-1566073771259-6a8506099945?q=80&w=400"
    },
    {
        "title": "Coco",
        "genres": "Animation, Family, Fantasy, Music",
        "overview": "Aspiring musician Miguel, confronted with his family's ancestral ban on music, enters the Land of the Dead to find his great-great-grandfather, a legendary singer.",
        "vote_average": 8.4,
        "release_date": "2017-11-22",
        "poster_url": "https://images.unsplash.com/photo-1511192336575-5a79af67a629?q=80&w=400"
    },
    {
        "title": "WALL·E",
        "genres": "Animation, Family, Sci-Fi",
        "overview": "In the distant future, a small waste-collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.",
        "vote_average": 8.4,
        "release_date": "2008-06-27",
        "poster_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=400"
    },
    {
        "title": "The Green Mile",
        "genres": "Drama, Fantasy, Crime",
        "overview": "The lives of guards on Death Row are affected by one of their charges: a black man accused of child murder and rape, yet who has a mysterious gift.",
        "vote_average": 8.6,
        "release_date": "1999-12-10",
        "poster_url": "https://images.unsplash.com/photo-1473163928189-364b2c4e1135?q=80&w=400"
    },
    {
        "title": "Se7en",
        "genres": "Crime, Mystery, Thriller",
        "overview": "Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his motives.",
        "vote_average": 8.6,
        "release_date": "1995-09-22",
        "poster_url": "https://images.unsplash.com/photo-1515694346937-94d85e41e6f0?q=80&w=400"
    },
    {
        "title": "Goodfellas",
        "genres": "Biography, Crime, Drama",
        "overview": "The story of Henry Hill and his life in the mob, covering his relationship with his wife Karen Hill and his mob partners Jimmy Conway and Tommy DeVito in the Italian-American crime syndicate.",
        "vote_average": 8.7,
        "release_date": "1990-09-19",
        "poster_url": "https://images.unsplash.com/photo-1533928298208-27ff66555d8d?q=80&w=400"
    },
    {
        "title": "Terminator 2: Judgment Day",
        "genres": "Sci-Fi, Action",
        "overview": "A cyborg, identical to the one who failed to kill Sarah Connor, must now protect her ten-year-old son John from a more advanced and powerful cyborg.",
        "vote_average": 8.5,
        "release_date": "1991-07-03",
        "poster_url": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?q=80&w=400"
    },
    {
        "title": "Alien",
        "genres": "Sci-Fi, Horror, Thriller",
        "overview": "The crew of a commercial spacecraft encounter a deadly lifeform after investigating an unknown transmission.",
        "vote_average": 8.4,
        "release_date": "1979-05-25",
        "poster_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=400"
    },
    {
        "title": "Aliens",
        "genres": "Sci-Fi, Action, Horror",
        "overview": "Decades after surviving the alien encounter, Ripley is sent with a team of space marines to investigate a colony on the planet where the creature was first found.",
        "vote_average": 8.3,
        "release_date": "1986-07-18",
        "poster_url": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?q=80&w=400"
    },
    {
        "title": "Psycho",
        "genres": "Horror, Thriller",
        "overview": "A Phoenix secretary embezzles $40,000 from her employer's client, goes on the run, and checks into a remote motel run by a young man under the domination of his mother.",
        "vote_average": 8.5,
        "release_date": "1960-06-16",
        "poster_url": "https://images.unsplash.com/photo-1505635330303-3195302cf604?q=80&w=400"
    },
    {
        "title": "Die Hard",
        "genres": "Action, Thriller",
        "overview": "An NYC cop visits his estranged wife and two daughters on Christmas Eve. He joins her at a holiday party in the headquarters of the Japanese-owned business she works for. But the festivities are interrupted by a group of terrorists who take over the exclusive high-rise, and everyone in it.",
        "vote_average": 8.2,
        "release_date": "1988-07-20",
        "poster_url": "https://images.unsplash.com/photo-1514565131-fce0801e5785?q=80&w=400"
    },
    {
        "title": "Mad Max: Fury Road",
        "genres": "Action, Sci-Fi, Adventure",
        "overview": "In a post-apocalyptic wasteland, a woman rebels against a tyrannical ruler in search for her homeland with the aid of a group of female prisoners, a psychotic worshiper, and a drifter named Max.",
        "vote_average": 8.1,
        "release_date": "2015-05-15",
        "poster_url": "https://images.unsplash.com/photo-1509316975850-ff9c5edd0cd9?q=80&w=400"
    }
]

with open("movies.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "genres", "overview", "vote_average", "release_date", "poster_url"])
    writer.writeheader()
    for row in movies_data:
        writer.writerow(row)

print("movies.csv has been successfully generated with 56 entries!")
