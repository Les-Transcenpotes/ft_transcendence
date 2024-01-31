# Token

2 types de tokens
access token -> permet l'acces -> vie plus courte
refresh token -> permet de regenerer -> vie plus longue


le JOT ou JWT ensemble de trois parties

1. headers
- information sur l'algorithme utilise
2. payload
- information sur le user
3. signature
- la signature utilise le header et le payload et y ajoute une cle secrete en base 64
- la cle est decryptable


# Django rest Framework


