# Mr Bean

An Unreal rendition of our project for the Internet Festival Quantum Game Jam 2021.

Details to come.

### Client

TODO
There's a basic Unity project we did a basic mock up with but no logic was implemented. We switched to Unreal.

### Server

This Python server offers a basic API to expose some Qiskit functionality for consumption in the game (client). For now it's just a basic QRNG (quantum random number generator).

#### Running
-------

1. Run the following commands
   ```
   pip3 install -r requirements.txt
   python3 -m MrBeanServer <servername> <port>
   ```

#### Usage Example
-------------

#### REST API
-------------

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

	Check the source code comments for more details.

### Credits

Bits of source code from the following projects were used:
https://github.com/vfp2/PodEntropyServer
https://github.com/ozaner/qRNG

