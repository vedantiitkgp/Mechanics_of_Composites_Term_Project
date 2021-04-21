# Mechanics_of_Composites_Term_Project

This Project is developed for Term Project Submission for Course ME60408 Mechanics of Composites and can be further used as part testing of laminates.

## Overview

This is an Application creating a series of simulation routines on composite data based on Classical Lamination Theory futher also running checks with Hashin failure criterion to test onset damage of laminates.

## Introduction

A composite material is a combination of two materials with different physical and chemical properties. When they are combined they create a material which is specialised to do a certain job, for instance to become stronger, lighter or resistant to electricity. They can also improve strength and stiffness. Micromechanics of composite is composed of lamina which has two basic components fibre and matrix.

![composition-of-composites-tenmat](https://user-images.githubusercontent.com/32813089/115611720-11491480-a308-11eb-94ec-2b65ad676be3.jpg)

Moving on to Mesomechanics there is a laminate structure forms a stack of Laminas .

![Aluminum-Composite-Materials](https://user-images.githubusercontent.com/32813089/115612791-46099b80-a309-11eb-83ae-7b9ba3f910eb.jpg)


## Application
This is the first Interface of Application which takes input data from the User regarding Stiffnes and Volume properties of Fibre as well as Matrix and calculates the effective properties of Lamina bulding the base for further calculations.

![Screenshot from 2021-04-11 14-56-18](https://user-images.githubusercontent.com/32813089/115613661-52422880-a30a-11eb-9659-301f69e09316.png)

This is the second Interface which further processing the properties of Lamina at diffrent angles and also plotting graphs for the similar case apart from that it also gives user the flexibility to change the mode of input to Q-Matrix (Stiffness) or S-Matrix (Compliance) of any plain lamina performing the similar steps.

![Screenshot from 2021-04-11 14-57-09](https://user-images.githubusercontent.com/32813089/115614770-b6b1b780-a30b-11eb-8f19-491a7407fb75.png)

Going further to the third interface where we design our laminate structure taking input of angles at which lamina are orinted in the stack. It also takes input the forces and moments acting at laminate to calculate effective stresses and strains in each lamina.

![Screenshot from 2021-04-11 14-58-06 (1)](https://user-images.githubusercontent.com/32813089/115615578-c4b40800-a30c-11eb-81e1-5f2ef47f043b.png)

Finally Building up for this we take input the strength properties of the material and testing our Hashin failure routine designed for plain Laminas guiding us which laminas have failed or what is the effective factor of safety.

![Screenshot from 2021-04-11 15-00-15 (1)](https://user-images.githubusercontent.com/32813089/115616297-ac90b880-a30d-11eb-9956-1a6e345b4752.png)

## Running Instructions

```shell
cd python
````

