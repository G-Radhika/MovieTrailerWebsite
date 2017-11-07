# -*- coding: cp1252 -*-  #
# While adding "poster_image and trailer_youtube" I guess some special charecters were added.
# Then I got an error saying non ASCII charecters are inserted and I ended up clicking "Edit my life" and voila above string was added to my code.
# StackOverflow told me this -->{"If you are file contains some special non ASCII character like "®"
# then IDE will add this line at the starting of your file.
# If you remove that line from the starting of file
# then non ASCII character wont be recognized."}

import media
import fresh_tomatoes
#I like Harry Potter! So why not make a movie website for it... :)
hp1 = media.Movie("Harry Potter & the Philosopher's Stone (2001)",
                  "Rescued from the outrageous neglect of his aunt and uncle,"
                  "a young boy with a great destiny proves his worth while attending"
                  "Hogwarts School of Witchcraft and Wizardry.",
                  "http://harrypotterfanzone.com/wp-content/2015/07/philosophers-stone-theatrical-poster.jpg",
                  "https://www.youtube.com/watch?v=VyHV0BRtdxo")
hp2 = media.Movie("Harry Potter & the Chamber of Secrets (2002)",
                  "Harry ignores warnings not to return to Hogwarts,"
                  "only to find the school plagued by a series of mysterious attacks"
                  "and a strange voice haunting him.",
                  "https://upload.wikimedia.org/wikipedia/en/c/c0/Harry_Potter_and_the_Chamber_of_Secrets_movie.jpg",
                  "https://www.youtube.com/watch?v=1bq0qff4iF8")
hp3 = media.Movie("Harry Potter & the Prisoner of Azkaban (2004)",
                  "It's Harry's third year at Hogwarts;"
                  "not only does he have a new Defense Against the Dark Arts teacher,"
                  "but there is also trouble brewing. Convicted murderer Sirius Black"
                  "has escaped the Wizards' Prison and is coming after Harry.",
                  "https://upload.wikimedia.org/wikipedia/en/b/bc/Prisoner_of_azkaban_UK_poster.jpg",
                  "https://www.youtube.com/watch?v=lAxgztbYDbs")
hp4 = media.Movie("Harry Potter & the Goblet of Fire (2005)",
                  "A young wizard finds himself competing in a hazardous tournament between"
                  "rival schools of magic, but he is distracted by recurring nightmares.",
                  "https://upload.wikimedia.org/wikipedia/en/c/c9/Harry_Potter_and_the_Goblet_of_Fire_Poster.jpg",
                  "https://www.youtube.com/watch?v=3EGojp4Hh6I")
hp5 = media.Movie("Harry Potter & the Order of the Phoenix (2007)",
                  "With their warning about Lord Voldemort's return scoffed at,"
                  "Harry and Dumbledore are targeted by the Wizard authorities"
                  "as an authoritarian bureaucrat slowly seizes power at Hogwarts.",
                  "https://upload.wikimedia.org/wikipedia/en/e/e7/Harry_Potter_and_the_Order_of_the_Phoenix_poster.jpg",
                  "https://www.youtube.com/watch?v=y6ZW7KXaXYk")
hp6 = media.Movie("Harry Potter & the Half-Blood Prince (2009)",
                  "As Harry Potter begins his sixth year at Hogwarts,"
                  "he discovers an old book marked as the property of the Half-Blood Prince"
                  "and begins to learn more about Lord Voldemort's dark past.",
                  "https://upload.wikimedia.org/wikipedia/en/3/3f/Harry_Potter_and_the_Half-Blood_Prince_poster.jpg",
                  "https://www.youtube.com/watch?v=sg81Lts5kYY")
hp7 = media.Movie("Harry Potter & the Deathly Hallows: Part 1 (2010)",
                  "As Harry races against time and evil to destroy the Horcruxes,"
                  "he uncovers the existence of three most powerful objects "
                  "in the wizarding world: the Deathly Hallows.",
                  "https://upload.wikimedia.org/wikipedia/en/2/2d/Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_1.jpg",
                  "https://www.youtube.com/watch?v=MxqsmsA8y5k")
hp8 = media.Movie("Harry Potter & the Deathly Hallows: Part 2 (2011)",
                  "Harry, Ron, and Hermione search for Voldemort's remaining Horcruxes"
                  "in their effort to destroy the Dark Lord as the final battle rages on at Hogwarts.",
                  "https://upload.wikimedia.org/wikipedia/en/d/df/Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_2.jpg",
                  "https://www.youtube.com/watch?v=mObK5XD8udk")

movies = [hp1,hp2,hp3,hp4,hp5,hp6,hp7,hp8]
fresh_tomatoes.open_movies_page(movies)
