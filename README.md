# Bean Jam

The Unreal rendition of our project titled "Bean Jam" for the Internet Festival Quantum Game Jam 2021.

By Team Bean 14th November 2021
“Team work makes the bean work”

Kartikeya Rambhatla (Powerhouse Coder, Quantum Physicist)
Olli Dahlgren (Coder, Quantum Physicist)
Simon McCorkindale (Coder, Aspiring Quantum Computerist)
Nicole Farrier (Quantum Physicist)
Sanjuktha Mukund (Game Designer)

## Story

Join Mr Bean on his epic quest through the small world of quantum to reach an even stranger and unknown realm. With quantum gates as his only ability to navigate the counterintuitive quantum world, he is on a mission to collect keys that some say lead to a realm no longer affected by the laws of quantum and classical physics. This lore - long since forgotten by the masses of human civilization -- comes from an ancient alien culture that refers to this realm as The Ultimate Observatory. A mystical place where the small is no longer small, a place from where the sole occupant can observe every particle in all the universes at once without affecting them and thus being of a truly omnipotent existence and having ultimate knowledge and power.

## Closing Ceremony

* [Presentation slides](https://docs.google.com/presentation/d/1KRUusqkLgXXsjbpE9Svb09ey73XNDuXC4r1JwuC9kTY)
* [YouTube demo video of the game](https://youtu.be/2pZ4idVhHxM)
* [YouTube of the closing ceremony and our presentation (from about 57:45~)](https://www.youtube.com/watch?v=l1FyNmBbRig&ab_channel=InternetFestival)

### Client

There's a basic Unity project we did a basic mock up with but no logic was implemented. We switched to Unreal.

### Server

This Python server offers a basic API to expose some Qiskit functionality for consumption in the game (client). It has basic QRNG (quantum random number generator) and Qiskit quantum circuit control functionality. We did not end up using this server in the version of the game we submitted to the IF Quantum Game Jam.

#### Running
-------

1. Run the following commands
   ```
   pip3 install -r requirements.txt
   python3 -m MrBeanServer <port> 
   ```

#### Usage Example
-------------

#### REST API
-------------

	##### QRNG

	http://localhost:<port>/api/get_random_bit_string
	Arguments: len (length (number of bits))
	E.g. http://localhost:<port>/api/get_random_bit_string?len=8

	http://localhost:<port>/api/get_random_int
	Arguments: min and max
	E.g. http://localhost:<port>/api/get_random_in?min=0&max=10

	http://localhost:<port>/api/get_random_int32

	http://localhost:<port>/api/get_random_int64

	http://localhost:<port>/api/get_random_float
	Arguments: min and max

	http://localhost:<port>/api/get_random_double
	Arguments: min and max

	http://localhost:<port>/api/get_random_complex_rect
	Arguments: r1, r2, i1, i2

	http://localhost:<port>/api/get_random_complex_polar
	Arguments: r and theta

	##### Qiskit with a 2 qubit circuit:

	Use same hostname/port like as above.

	/api/qlogic/begin_play
    /api/qlogic/init
    /api/qlogic/collapse
    /api/qlogic/get_probv
    /api/qlogic/reset0
    /api/qlogic/reset1
    /api/qlogic/X0
    /api/qlogic/H0
    /api/qlogic/Y0
    /api/qlogic/Z0
    /api/qlogic/S0
    /api/qlogic/CNOT0
    /api/qlogic/X1
    /api/qlogic/H1
    /api/qlogic/Y1
    /api/qlogic/Z1
    /api/qlogic/S1
    /api/qlogic/CNOT1

    ##### API server status:
    /api/status

	Check the server source code comments for more details.

### Credits

Bits of source code from the following projects were used:
https://github.com/vfp2/PodEntropyServer
https://github.com/ozaner/qRNG

