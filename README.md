ahkab
=====

a SPICE-like electronic circuit simulator written in Python

The code should be easy to read and modify, the main language is Python 2.x and it is platform-independent.

### News! ###

 * The project [moved to GitHub](https://github.com/ahkab/ahkab). 
 * `ahkab` can now be run stand-alone with a netlist file or _within Python scripts as a library_. This will likely become the preferred way in the future.

See **[this butterworth filter simulation](https://github.com/ahkab/ahkab/wiki/SimulatingThePythonWay)** for an example/tentative tutorial.

### Supported simulations: ###
  * Numeric:
    * **Operating point**, with guess computation to speed up the solution. See example: [Downscaling current mirror](https://github.com/ahkab/ahkab/wiki/OPexample)
    * **DC sweep**
    * **Transient analysis**, available differentiation formulas: implicit Euler, trapezoidal, gear orders from 2 to 5. See for example the [[simulation of a Colpitts Oscillator](https://github.com/ahkab/ahkab/wiki/Transient_simulation_example).
    * **AC analysis**
    * **Periodic steady state analysis** of non-autonomous circuits, _time_ _domain_ shooting and brute-force algorithms.
  * Symbolic: 
    * **Small signal analysis**, AC or DC, with extraction of transfer functions, DC gain, poles and zeros. Various [symbolic analysis examples on this page](https://github.com/ahkab/ahkab/wiki/SymbolicExamples).

The results are saved to disk, plotted or printed to stdout and can be read/processed by the most common tools (eg. [Octave](http://www.gnu.org/software/octave/), [gnuplot](http://www.gnuplot.info/), [Matlab](http://www.mathworks.com/products/matlab/), [gwave](http://www.telltronics.org/software/gwave/) and others)

###Download and install###

There are no packages for the time being (this program is at an early development stage). Go to [ahkab on github](https://github.com/ahkab/ahkab) and follow the instructions to check out the code. You can find the list of the dependencies in the [Install notes](https://github.com/ahkab/ahkab/wiki/Install_Notes).

###Run standalone###

    $ python ahkab -o graph.dat <netlist file>`

See `ahkab --help` for command line switches.

###Documentation###

The simulator can either be run from the command line with a netlist file or included in a python script. Both possibilities will be maintained for the foreseeable future. 

Refer to the [netlist syntax page](https://github.com/ahkab/ahkab/wiki/NetlistSyntax) for how to write the netlist files that describe the circuit. Experience with running SPICE or other commercial simulators can be useful.

The latter option is shown briefly in the **[Simulating the Python way](https://github.com/ahkab/ahkab/wiki/SimulatingThePythonWay)** wiki page. The code comes with docstrings associated with _most_ functions, type `help(ahkab.function_name)`.

### Contributors ###
Giuseppe Venturini (@ggventurini on GH) Ian Daniher (@itdaniher, also on GH)

### Bugs and patches ###

Note that _I often add new functionality at the expense of breaking stuff_. Most likely I will introduce a new feature even if that means breaking a couple of others. It should get fixed soon, but if you have a bit of time to spare, you can send me a pull request or a patch. :)

Does it work? Bugs? Do you have patches? Did you run some noteworthy simulation? Let me know! Feedback is very welcome, my [email address](http://tinymailto.com/5310) is available after a captcha.
