import fresh_tomatoes
import movies

Beauty_and_the_beast = movies.Movie("Beauty and the beast",
                                    "A story of a bright, beautiful \
                                     and independent young woman",
                                    "http://t2.gstatic.com/images?q=tbn:ANd9 \
                                     GcT7w1Dj-lkTL1CooOXihJ3WBIxyt3K9H6UZ08Kt \
                                     jv8Ba3gLgC7B",
                                    "https://www.youtube.com/watch? \
                                     v=e3Nl_TCQXuw")
# print(Beauty_and_the_beast.storyline)
Guardians_of_the_Galaxy_2 = movies.Movie("Guardians of the Galaxy 2",
                                         "American superhero film \
                                          based on the Marvel Comics",
                                         "http://t3.gstatic.com/images?q=tbn:A \
                                          Nd9GcQXZE44ioeZHmwyJMeBa3rXFyOWT \
                                          Ne3ZnoYUK0tSkdkECpX-v7P",
                                         "https://www.youtube.com/watch? \
                                          v=2cv2ueYnKjg")
# print(Guardians_of_the_Galaxy_2.storyline)
# Guardians_of_the_Galaxy_2.show_trailer()
Annabelle_Creation = movies.Movie("Annabelle Creation",
                                  "supernatural horror film",
                                  "http://t2.gstatic.com/images?q=tbn:A \
                                   Nd9GcSFJXO-WgGmu29wKPaaR2lPco4z3krUU_A \
                                   qiktmz4XtxGvys3Cn",
                                  "https://www.youtube.com/watch? \
                                   v=KisPhy7T__Q")
# print(Wonder_Woman.storyline)
# Wonder_Woman.show_trailer()
Wonder_Woman = movies.Movie("Wonder Woman",
                            "Rise of a Warrior",
                            "http://t1.gstatic.com/images?q=tbn:ANd9GcQcCAO \
                             mt-FsRsR8GebIzI67qSvdQ2JLYDRLxeAcbH-541fzqq1H",
                            "https://www.youtube.com/watch? \
                             v=VSB4wGIdDwo&t=103s")
# print(Dangal.storyline)
# Dangal.show_trailer()
Dangal = movies.Movie("Dangal",
                      "sports drama film based on true story",
                      "http://t3.gstatic.com/images?q=tbn:ANd9GcQIXnFlB \
                       KGWT1ByyIu3qfxX6opQX6BmeeU_qsiE3X8rX9ZRr63r",
                      "https://www.youtube.com/watch?v=x_7YlGv9u1g")
# print(Dear_zindagi.storyline)
# Dear_zindagi.show_trailer()
Dear_zindagi = movies.Movie("Dear zindagi",
                            "Love you zindagi",
                            "http://t2.gstatic.com/images?q=tbn:ANd9GcQlZ4YZ7 \
                             wNla7O6kQQQ83OAcEDsv1_S1a_euSbenWr_FpkJW_6D",
                            "https://www.youtube.com/watch?v=5DkO7ksXY8E")
movies = [Beauty_and_the_beast, Guardians_of_the_Galaxy_2, Annabelle_Creation,
          Wonder_Woman, Dangal, Dear_zindagi]
fresh_tomatoes.open_movies_page(movies)

