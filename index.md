# Welcome to Genetic Algorithm Project of Course FENG-498

Hi! We are engineering applicants Eyup Batuhan Sevinc and  Efe Berk Dinc. We are studying Sofware/Computer Engineering at Izmir University of Economics. Genetic Algorithm Project is our final project. In this project we are making a program that will make genetic algorithm calculations easier.

!["Program"](https://i.hizliresim.com/4c7j4uc.png)

# Abstract

Genetic algorithms is a wide subject to study. Depending on the size and the complexity of a problem, they might take a long time to implement, run and get results. Also, programmers can’t always reach a reliable, open-source GA testing tool and test their own GAs with their own parameters. The following project report focuses on GAs, examining their working principles and the development of a GA testing tool with GUI (Graphic User Interface) which will enable the users to test their GAs with the extra implementation effort and time kept as minimal as possible. Different selection, crossover and mutation methods are studied both in theory and in practice, provided with their relevant tables and codes.

## Introduction


Genetic algorithms (GAs) started to be used after the studies of John Holland and his friends, in the 1970’s. As it can be understood from this sentence alone, GAs have been with us for a very long time, but their principles go back even longer. To understand GAs -what they are and how they work- we will have to look at the evolution. 

The principle mentioned above is the “survival of the strongest (the fittest) individual” and the main point GAs make. Genetic algorithms consist of evolutionary steps, which are forming a population, making a selection, performing a crossover, putting the off-springs into the new population and continuing this cycle. Despite the almost “biological” approach, GAs are about mathematics and programming. Their main purpose is to find solutions (optimal or best solutions) to complex optimization problems. However, there are certain differences between GAs and classic optimization methods. In an optimization scenario, the algorithms are defined for the problem from the start. We simply adjust our variables and try to come up with a solution. On the other hand, we can modify our algorithm in GAs. They are given a couple of parameters and functions to work with, and we expect them to come up with the result, often using machine learning. A typical GA consists of the following steps:

 1. Creating the initial population, 
 
 2. Calculating the fitness value for each chromosome (made up by a certain amount of genes), 

 3. Applying the crossover, mutation and other relevant operators, 

 4. Finding the fitness value for each new chromosome, 3 

 5. Ranking the chromosomes based on their fitness levels (and based on the specific type of question at hand), 
 
  6. Returning to the 3rd step and continuing this cycle until the desired output and fitness values are reached. 
      
   In our project, other than exploring the GAs and their principals, we are also looking to develop an improved program in general. Genetic algorithms are vast-- one could write a GA for almost every problem that fits the type, which is definitely a lot. We are developing a GUI (Graphic User Interface) tool to help programmers test their GAs and play around with parameters, functions, and easily reach solutions by saving them time. As we will discuss this point in the further sections of this report, we will also be including previous studies conducted and programs created for GA GUI tools.

## Problem Statement

GAs require some time to write, especially the complex ones, and the subject in general might be exhausting for a beginner. There are too many options to choose from regarding the selection and crossover functions, and it is time consuming to code and implement all of them to use. Some options might be overlooked, missed entirely.

## Motivation

Developers and coders should always look for easier ways to get the job done. Implementing each and every thing when they can simply use a GUI tool would be a bad move. The GA GUI tool that we are developing will include all functions (selection, crossover, hyperparameter selections and other types) and they will be presented to the user so they can benefit from it. It is all up to the user and their own preference for their GA. This way, anyone who has a GA to implement, test and solve, will be able to save so much time.

## Literature Review

Zoltán Tóth worked on a program called GraphGEA (Graph-Generic Evolutionary Algorithms) developed with GTK API, which offers many selection, crossover and other applications of GAs to the users-- all selected from the interface he provided. The parameter and algorithm selection mentioned there happens with dialog boxes shown to the user. GraphGEA also enables the user to save and store their deserved parameters or parameter sets. Then, the results can be observed from the graphs and images the program draws. Tóth defines the program as an educational program which can help many students and researchers test their own problems. His work is very close to ours in purpose and the way it works, so we will be studying the results he obtained and we believe that this will help us a lot while analysing our own work. We will also include as many algorithms as we can (selection, crossover, mutation, etc.), visualize the data set of any result (with graphs) and try to give the users a good experience. [1]



Gardner and Simon developed an evolutionary algorithm sandbox with GUI on Adobe® Flex® and made it possible for the users to test their algorithms and run simulations. The users are free to choose the parameters and helpful algorithms they want to use and are able to watch the simulation run and see the results of the generations. They also add that this program can be extended without much trouble to make it applicable for many other problems. Just like the previous work stated above, we will be using this study as a guide as well. [2]

Farooq and Siddique focused on the user interfaces of interactive GAs. They worked on the graphical representations and details of IGAs. They made a few points about machine learning, applications of fashion design, 3D object modeling and so on. They discussed the current position of IGAs and their future, how they are expected to develop. We will not be providing such detailed 3D models for the GAs, however from this study, we can get a few tips on our own interface and how we can implement the graphical parts, taking inspiration from their opinions and research on IGA interfaces. [3]

Collet and Schoenauer pointed out the lack of programs which present the user the opportunity to change their parameters and algorithms easily through a GUI, in their own study. They talk about GUIDE (Graphical User Interface for DREAM Experiments), a unified program of evolutionary algorithms. They also claim that GUIDE is user-friendly and a good start for students who want to get into the world of EAs and GAs. Also from this study, we can get tips and use it as our guide to unifying many parameters and descriptions of GAs. [4]

John Runwei Cheng and Mitsuo Gen worked on an extensive study of speeding GAs up with GPU usage. Their research contains joint architectures of GPU-CPU models. They also talk about the similarities and differences between running parallel GAs on each case. Finally, they include a concept which they explain as “granularity of parallelism” and work on the acceleration of such structures when placed in GPU. From this study, we can learn more about GPU and CPU, as we will try to make our operations and program parallel, because this way we will be able to run our genetic algorithms much faster. [5]

Juan C. Quiroz et al. talked about “user fatigue” that might be experienced in interactive GAs. They argued that users might face such a problem where they have to make so many decisions for each generation and more. They came up with two steps as a solution. The first step is to make the users choose the best and the worst interface designs from nine different options. Then, the second step is having the user make decisions every “t” generations, not in each. They explained that their aim is to help the designers with an innovative approach. His work can help us analyze GAs and their relationship with generating GUIs, therefore helping us understand more about both concepts. [6]

Jun-Woo Kim used a GA to create a job shop scheduling system that comes with a detailed interface. He mentioned that this type of scheduling problems are quite hard to solve and they can get complicated. In his work, he used a “candidate order” based GA to implement constraints easier. His interface also came with graphical representations, which helped the users visualize the schedule by playing around with nodes and arcs, as well as Gannt charts. Kim’s study and program structure will guide us through interface designs and help us in coming up with different graphs and images to visualize the results or outcomes of GAs. [7]

Z. J. Feng and C. Dong aimed to find molecular crystal structures from powder diffraction data. Their software GEST included the evolution function of genetic algorithms, which they explained as a modified function of “Bragg R factor”. They said that their interface is user-friendly and the whole program is open-source. [8]

Li and Huang planned the path of a mobile robot, using GAs. They used a static environment and tried to find the shortest path for the robot. They tested how adaptive it was and how it responded to the changes in the algorithm. In the end, they concluded that this method of using improved genetic algorithms is useful for planning the path of robots. [9]

Hinterding et al. worked on numeric functions and their self-adaptive GAs. They argued that self adaptation is becoming quite important in evolutionary computations. Their work focused on 6 letting the GA learn about the problem, come up with mutation probabilities and population sizes on its own. They proceeded to state that their results show a positive feedback on how applicable this method is for numeric functions. [10]

# Methodology

In our project, we used two programming languages; Python and Java. We started off with Java, explored the various functions and methods, then moved to Python and decided to continue with it (The relevant codes and schemes are provided in the Appendix section of the report).

#### Java & Python Platforms
 The Java programming language is harder to implement, compared to Python. We tried our hand in arrays, array lists and other functions such as crossover and selection functions. Each GA is specific to its own, therefore despite the similarities between those algorithms and problems, one would have to implement most things from scratch. Python offers an easier approach especially in genetic algorithms. We played around with lists, showing everything much more clearly and observed that this platform is much more effective and fast compared to Java. It also made everything easier for us with its libraries.

## Genetic Algorithms and Operations
 ### Selection Operation

 The various types of selection make it possible for us to select chromosomes to perform a crossover. They might have different probabilities and different ways of working. Below are the selection operations that we worked with.

### Roulette Wheel Selection 
As it can be understood from the name, the chromosomes enter the roulette wheel and with a certain probability attached to randomness, they are chosen from their groups. This method is also known to be stokastik örneklem [11].

 ![**Figure 3.2.1.1 Roulette Wheel Selection [15]**](https://lh4.googleusercontent.com/G4V55EhHQ0S2A6uQ0uo_frw4mPD1av2GIIEg28pqnlRmZqHDpo_QSmheUsZAEQ4zYRxYmu3GZuPYGF7KNm2QjM5R4j_-VoyqrH89GR2tRXjY-Q4-cqnIPycUuLFWixcrkAX5xWBe)

*****Figure 3.2.1.1 Roulette Wheel Selection [15]*****

### Tournament Selection

Based on any real tournament, the chromosomes are arranged with respect to how well their fitness values fare. It is quite efficient and applicable. After the evaluation of their fitness values, the strongest individuals are gathered and put in the new population. The advantage of this particular method is the way it prevents weak individuals from participating in a crossover and letting the strongest individuals come through and proceed. The wider the tournament is, the more efficient the selection gets [12].

![enter image description here](https://lh3.googleusercontent.com/clXoRYIKutqO2kZBgYvKGpdhTIL5BZSqDJjTaMXSLh0JuFdzIYr5P2Xu8oknE2aiUwYC67KM-8WRkl4fImyoMHMlxVUibtrzduf_Mzw3dmhv3LEWf92Hrbru9lF4QBzmE7btzmcL)

*****Figure 3.2.1.2 Tournament Selection [16]*****

## Crossover Operation

Crossover operation is one of the most important steps of a GA. This operation takes two chromosomes and performs the traditional crossover method, dividing the chromosome and matching the genes between themselves with respect to the defined method. Each new chromosome carries the genes of previous generations. Below are the crossover methods we have written and tried.

### Single Point Crossover

In this type, the chromosomes are divided into half from a single point and matched between themselves.

![](https://lh5.googleusercontent.com/YxyBzJTqoAz9opc_H2FZAsmH38sDujhwO8OElUSWXzCEt9ak9OQg3Ejrip_d1sOXQFqB9VCzboKiqjUKXC0kMAikLqdtyZYspWMD8oK14-x6LrLNalVNEHrB2PUisRHNimidWUAA)

![enter image description here](https://lh4.googleusercontent.com/cho2gcRRlrja4LJJdzEkyFJny6Eq1_4sBuezDCeuAziFodn1QSHpsEyByDiY5F_tfuwxaAKkHICZzEM4iQgRAjSnA9xzie-SWYsKmeydYn-rSSoaHi-SFuBq3KZx_kSklKyU_iHp)

*****Figure 3.2.2.1 Demonstration of SP crossover [17]*****


### Two Point Crossover

In this type of crossovers, the chromosomes are divided from two points and matched between themselves. The genes between these two points are swapped to get new off-springs [13]. 


![](https://lh6.googleusercontent.com/BTUr9StVSv8VdacqA4hpzCpTOoMTMNf33H8Mvg8TWwH67g2iS8V6tt44wvrERXDLHYgr3BxUpNGUl-ShbTQkXzRApxgMYhkJXNh60MBCFIiCUC4QLqzZHUz9djrxscHoB9OxqCHU)

![](https://lh6.googleusercontent.com/Unt_QWNwb9FET65UVb18ditfRyG1o97uC_kgBhvkbJxiNTJJ-POc_5i2-OlkQHZ4bbNoB8OkXjldzTQE7X4r61PnDiC3RBxwYX492stXYE1Dbc5jq4t-5foWyF60yUcELl5FJOwz)


*****Figure 3.2.2.2 Demonstration of TP crossover [17]*****


### Multiple Point Crossover

In multiple point crossovers, there are three or more division points on chromosomes. The off springs end up with more diverse genes.

![](https://lh6.googleusercontent.com/SdIP8x6-kkzngSg6P80wEKciWIp9pUla0mLCM5gnmP4vztIOoOQsC9PbkZbfLNenlQq50lAC1SVLkWn80k4X9uWcEEMKKoXYt-8aegwUhxpXlN2psDEf5Rc-8K8875y0AY0Nlj2l)

![](https://lh4.googleusercontent.com/kfZjxznMYByi1HaUKWJ6C2RUZ64ZLOdnL7zMMlbJSFiLZKDV1J1C-ijuH_ao92_kIYqIIJpTzLLAAagA7WaYJknmn4YDKwXdqCNt7zStytzvpd3Al-N0-0j57BulxdW_rwCwUwYt)

*****Figure 3.2.2.3 Demonstration of MP crossover [17]*****

### Uniform Crossover

In this type of crossovers, the relevant genes (bits) are swapped with the conditions set by the function. For example, “1” says that the gene will be copied from the first parent, while “0” means that the gene will be copied from the second parent.

![](https://lh4.googleusercontent.com/ZZmWIOz4rK_E0DDwzkz_IVng7NvQ-yq_bBX9BpaAp0JR1fDJRyqcxjDFIlbfdrq0VcDxYy2Ad9GpgF8Zwxd9lcQXBaUsI2shMgpekwpasIxp4sAvAw92ApXCwnEYLq1aSOYkH1ZZ)

![](https://lh4.googleusercontent.com/O_kGB_yasxTRC03wjNFM4aZZjWGB4MQuyomRF8cpINoOjx-ErJTH-3p_dPTHon6oUECGiyGoq36mVkfshNm9lVN2ewMAqSiXmCh13jdKZpXcwIJSojFBNF7fBmKI0oHBQ08chUpk)

![](https://lh5.googleusercontent.com/xBiQa6I-bml25m3CN1lxT6I-2Vm-cgGWWgerS7FD9xCZ8l9n_ZtriEQIxB4NeR7487D2t5N4zyuH8d28Th5heuAWlUWy5iK-Y0dRYqDGpmm3lxav-lifeynd1w9jmFrK8nm724Zj)

*****Figure 3.2 Demonstration of uniform crossover [17]*****

### Mutation Operation

Mutation is used to mutate, change, a particular gene inside a chromosome and increase the gene variation inside the population. It has a probability, which is defined by the user or given in a problem, and it helps us get different results based on this probability value. However, the results might vary so much that the values might be too different than what we originally planned, and we might stray away from our desired outcome.



Therefore, the mutation probability must be kept in check as it can both improve and destroy our solutions. In a typical GA, the mutation frequency is chosen between 0.01 to 0.001 [14].

![](https://lh4.googleusercontent.com/FXkILrn98fFRYf3uTr7DM3RrprgRNbO5EutwtHg4ZOLvRzYpIiKC1YZ7e2Y_kTVVTr9EVXa4No5tz8xM7DtRGF5L5nHzgWgiQ7S_3dYjtVkzz9B1shOT1QFcYFW950oS-5bTZitm)

![](https://lh5.googleusercontent.com/oI3NHQ5ppRSxeLNv5XwWjLjQQzMh4VBH1hLJpfHIoAKMz7V3kb6OVtXDg5n5kFZ1I2AG2KzeeTRHMIWUvyCEHvbCbJas-l8NxXjiT2RuWLcDBgpzfCUQbmle1wH6O0Rx5RO5ixWV)

*****Figure 3.2.3 Demonstration of mutation with the parent (above) and child (below) [17]*****

### Elitism Operation

The programmer might include this operation in the algorithm, as we will do so on our own. Elitism gives us an opportunity to pass the best individuals called “the elite” right onto the next generation without any additional operations performed on them. This way, we preserve the fittest individuals and protect them against a wrong placed mutation and lowering their fitness scores.

# Conclusions

Genetic algorithms help us carry a problem into the virtual space of coding, try many solution methods and get the best results we can possibly have. They keep evolving without being stuck at a final solution, therefore our solution set is almost infinitely wide. We can also include artificial intelligence in this matter, an advanced copy of the human brain. If they are granted the methods to learn, they can develop themselves and their outcomes without being tied to any other thing. A projection of AI shows itself in our project too, inside our GAs. It can be implemented into the program and improve the solution sets.

In our project, after examining many different types of GAs, we focused on a general picture, a main GA GUI tool. The first stop was to work on the crossover operation. Crossover operations are considered to be one of the most important parts of a GA. This operation helps us merge the best genes and aspects of the chromosomes and create better individuals, and better generations. The second point we worked on was selection algorithms. Having observed the way selection works in a GA, we decided that being able to select the best chromosomes somehow, will definitely improve our solutions from the very beginning of the process. Another point we worked on is the mutation operator. We observed that playing around too much with the mutation probability might result in worse outcomes, so we tried to keep that value under control.



All in all, it is possible to talk about the advantages and disadvantages of GAs based on our experience working with them,

➢ GAs can work with many parameters at once,

➢ GAs can process complex objective functions without getting confused with local minimum and maximum values or additional parameters,

➢ GAs offer a wide variety of applications, from the beginner level to the advanced. However,

➢ GAs rely on probabilities and randomness, therefore it might take a very long time for them to find solutions,

➢ GAs are not prefered if the user wants to get to a certain solution,

➢ GAs might not be able to find the best solution if they are restricted with too many constraints.

During the fall term, we tried to work with what we had without straying away from our goals while trying to be as efficient as possible-- and we will continue to do so in the following term. There is still much to learn, but now that we have experienced many things regarding GAs, we feel much more confident to go after our future plans of developing a GA GUI tool for any user who wants to test their genetic algorithms.

# References

[1] Tóth, Z. (2003). A graphical user interface for evolutionary algorithms. Acta Cybernetica, 16(2), 337-365. Retrieved from https://cyber.bibl.u szeged.hu/index.php/actcybern/article/view/3628

[2] B. G. Gardner and D. Simon (2009), "Evolutionary algorithm sandbox: A web-based graphical user interface for evolutionary algorithms," 2009 IEEE International Conference on Systems, Man and Cybernetics, San Antonio, TX, pp. 577-582, doi: 10.1109/ICSMC.2009.5346657. https://ieeexplore.ieee.org/document/5346657

[3] Humera Farooq, Muhummad Tariq Siddique (2014), A Comparative Study on User Interfaces of Interactive Genetic Algorithm, Procedia Computer Science, Volume 32, Pages 45-52, ISSN 1877-0509, https://doi.org/10.1016/j.procs.2014.05.396.

(https://www.sciencedirect.com/science/article/pii/S1877050914005961)

[4] Collet P., Schoenauer M. (2004), GUIDE: Unifying Evolutionary Engines through a Graphical User Interface. In: Liardet P., Collet P., Fonlupt C., Lutton E., Schoenauer M. (eds) Artificial Evolution. EA 2003. Lecture Notes in Computer Science, vol 2936. Springer, Berlin, Heidelberg. https://doi.org/10.1007/978-3-540-24621-3_17

[5] John Runwei Cheng, Mitsuo Gen (2019), Accelerating genetic algorithms with GPU computing: A selective overview, Computers & Industrial Engineering, Volume 128, Pages 514- 525, ISSN 0360-8352, https://www.sciencedirect.com/science/article/pii/S036083521830665X  [6] J. C. Quiroz, S. J. Louis, A. Shankar and S. M. Dascalu (2007), "Interactive Genetic Algorithms for User Interface Design," 2007 IEEE Congress on Evolutionary Computation, Singapore, 2007, pp. 1366-1373, https://ieeexplore.ieee.org/abstract/document/4424630

[7] Kim, J.W. (2015), Developing a job shop scheduling system through integration of graphic user interface and genetic algorithm. Multimed Tools Appl 74, 3329–3343. https://link.springer.com/article/10.1007/s11042-014-1965-7


[8] Feng, Z. J. & Dong, C. (2007), GEST: A Program for Structure Determination from Powder Diffraction Data Using A Genetic Algorithm, Journal of Applied Crystallography, https://scripts.iucr.org/cgi-bin/paper?ko5035

[9] Y. Li, Z. Huang and Y. Xie (2020), "Path planning of mobile robot based on improved genetic algorithm," 2020 3rd International Conference on Electron Device and Mechanical Engineering (ICEDME), Suzhou, China, pp. 691-695, doi: 10.1109/ICEDME50972.2020.00163. https://ieeexplore.ieee.org/abstract/document/9122093

[10] Hinterding R., Michalewicz Z., Peachey T.C. (1996), Self-adaptive genetic algorithm for numeric functions. In: Voigt HM., Ebeling W., Rechenberg I., Schwefel HP. (eds) Parallel Problem Solving from Nature — PPSN IV. PPSN 1996. Lecture Notes in Computer Science, vol 1141. Springer, Berlin, Heidelberg. https://doi.org/10.1007/3-540-61723-X_1006

[11] Goldberg, D.E. (1989). Genetic Algorithms in Search, Optimization, and Machine Learning, Addisson-Wesley, Reading. MA, 412-415

[12] Michalewich, Z. (1994). “Genetic Algorithms + Data Structures = Evolutions Programs”, Springer-Verlag, Berlin. 340-353

[13] Tomassini, M. (1996). Evolutionary Algorithms, Lecture Notes in Computer Science. Springer-Verlag, Berlin, 19-47.

[14] Çunkaş, M. (2006). Genetik Algoritmalar ve Uygulamaları Ders Notları ; Aksu,Ö.(2008). Yeni Bir Paralel Genetik Algoritma Modeli Ve Analog Devre Tasarımına Uygulanması Yüksek Lisans Tezi, Kayseri: Erciyes Üniversitesi, Fen Bilimleri Enstitüsü, 38s.

### Figures

[15] Figure 3.2.1.1 http://www.edc.ncl.ac.uk/highlight/rhjanuary2007g02.php  [16] Figure 3.2.1.2 https://www.slideshare.net/riyadparvez/selection-in-evolutionary-algorithm  (pg 8 of 55)

[17] Figure 3.2.2.1 to Figure 3.2.3 https://core.ac.uk/download/pdf/159313423.pdf  [18] (Appendix section) Courtesy of our supervisor Kaya OĞUZ, Robby the Robot’s Genetic Algorithm
