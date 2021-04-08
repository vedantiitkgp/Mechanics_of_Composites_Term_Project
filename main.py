from math import sqrt,cos,sin
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
#### Sub routine 1 ####

##### Calculating effective properties of unidirectional composite lamina ####
## Inputs - E1_fibre,E2_fibre,nu12_fibre,nu23_fibre,G12_fibre,G23_fibre,E_matrix,nu_matrix,G_matrix,Volume_fraction_fibre
## Outputs - E1 ,E2, E3, nu12, nu13, nu23, G12, G13, G23 of effective lamina
def effective_lamina_properties(E1_fibre,E2_fibre,nu12_fibre,nu23_fibre,G12_fibre,G23_fibre,E_matrix,nu_matrix,G_matrix,Volume_fraction_fibre,chamis_correction=False):
    E1 = Volume_fraction_fibre*E1_fibre + (1-Volume_fraction_fibre)*E_matrix
    E2 = (E2_fibre * E_matrix )/(E2_fibre*(1-Volume_fraction_fibre)+E_matrix*Volume_fraction_fibre)
    E3 = (E2_fibre * E_matrix )/(E2_fibre*(1-Volume_fraction_fibre)+E_matrix*Volume_fraction_fibre)
    nu12 = (1-Volume_fraction_fibre)*nu_matrix + Volume_fraction_fibre*nu12_fibre
    nu13 = (1-Volume_fraction_fibre)*nu_matrix + Volume_fraction_fibre*nu12_fibre
    nu23 = (1-Volume_fraction_fibre)*nu_matrix + Volume_fraction_fibre*nu23_fibre
    G12 = (G12_fibre * G_matrix)/(G12_fibre*(1-Volume_fraction_fibre)+G_matrix*Volume_fraction_fibre)
    G13 = (G12_fibre * G_matrix)/(G12_fibre*(1-Volume_fraction_fibre)+G_matrix*Volume_fraction_fibre)
    G23 = (G23_fibre * G_matrix)/(G23_fibre*(1-Volume_fraction_fibre)+G_matrix*Volume_fraction_fibre)
    if chamis_correction :
        E22 = (E2_fibre * E_matrix )/(E2_fibre*(1-sqrt(Volume_fraction_fibre))+E_matrix*sqrt(Volume_fraction_fibre))
        E22 = (E2_fibre * E_matrix )/(E2_fibre*(1-sqrt(Volume_fraction_fibre))+E_matrix*sqrt(Volume_fraction_fibre))
        G12 = (G12_fibre * G_matrix)/(G12_fibre*(1-sqrt(Volume_fraction_fibre))+G_matrix*sqrt(Volume_fraction_fibre))
        G13 = (G12_fibre * G_matrix)/(G12_fibre*(1-sqrt(Volume_fraction_fibre))+G_matrix*sqrt(Volume_fraction_fibre))
        G23 = (G23_fibre * G_matrix)/(G23_fibre*(1-sqrt(Volume_fraction_fibre))+G_matrix*sqrt(Volume_fraction_fibre)) 
    return E1,E2,E3,nu12,nu13,nu23,G12,G13,G23

#### Sub routine 2 ####

##### Calculating S and Q matrix for lamina ####
## Inputs -E1,E2,E3,nu12,nu13,nu23,G12,G13,G23
## Outputs - Q(3x3 Matrix), S(3x3 Matrix)   

def stiffness_compliance_matrix(E1,E2,E3,nu12,nu13,nu23,G12,G13,G23):
    S_matrix = np.zeros((6,6),dtype=float)
    S_matrix[0][0] = 1/E1
    S_matrix[0][1] = (-1*nu12)/E1
    S_matrix[0][2] = (-1*nu13)/E1
    S_matrix[1][0] = (-1*nu12)/E1
    S_matrix[1][1] = 1/E2
    S_matrix[1][2] = (-1*nu23)/E1
    S_matrix[2][0] = (-1*nu13)/E1
    S_matrix[2][1] = (-1*nu23)/E1
    S_matrix[2][2] = 1/E3
    S_matrix[3][3] = 1/G23
    S_matrix[4][4] = 1/G13
    S_matrix[5][5] = 1/G12

    nu21 = (nu12 * E2)/E1
    nu31 = (nu13 * E3)/E1
    nu32 = (nu23 * E3)/E2
    Q_matrix = inv(S_matrix)

    S_planar = np.zeros((3,3),dtype=float)
    S_planar[0][0] = S_matrix[0][0]
    S_planar[0][1] = S_matrix[0][1]
    S_planar[1][0] = S_matrix[1][0]
    S_planar[1][1] = S_matrix[1][1]
    S_planar[2][2] = S_matrix[5][5]
    Q_planar = inv(S_planar)
    return Q_planar,S_planar

#### Calculate the modulus and elastic propties at another angle ####
## Inputs - Q_matrix(3X3 Matrix)/S_matrix(3X3 Matrix)/Material_Propties([E1,nu12,E2,G12])
## Outputs - Ex,nuxy,Ey,Gxy,etaxy_x,etaxy_y
def effective_lamina_properties_angle(Q_matrix=False,S_matrix=False,Material_properties=False,data=1,angle=0):
    m = np.cos(angle)
    n = np.sin(angle)
    if Q_matrix == True:
        data = inv(data)
        Ex = 1/(pow(m,4)*data[0][0]+pow(m,2)*pow(n,2)*(data[2][2]+2*data[0][1])+pow(n,4)*data[1][1])
        nuxy = Ex*(-pow(m,2)*pow(n,2)*(data[0][0]+data[1][1]-data[2][2])-data[0][1]*(pow(m,4)+pow(n,4)))
        Ey = 1/(pow(n,4)*data[0][0]+pow(m,2)*pow(n,2)*(data[2][2]+2*data[0][1])+pow(m,4)*data[1][1]) 
        Gxy = 1/(4*pow(m,2)*pow(n,2)*(data[0][0]+data[1][1]-2*data[0][1])+pow(pow(m,2)-pow(n,2),2)*data[2][2])
        etaxy_x = Ex*(pow(m,3)*n*(2*data[0][0]-2*data[0][1]-data[2][2])-pow(n,3)*m*(2*data[1][1]-2*data[0][1]-data[2][2]))
        etaxy_y = Ey*(pow(n,3)*m*(2*data[0][0]-2*data[0][1]-data[2][2])-pow(m,3)*n*(2*data[1][1]-2*data[0][1]-data[2][2]))
    
    if S_matrix == True:
        Ex = 1/(pow(m,4)*data[0][0]+pow(m,2)*pow(n,2)*(data[2][2]+2*data[0][1])+pow(n,4)*data[1][1])
        nuxy = Ex*(-pow(m,2)*pow(n,2)*(data[0][0]+data[1][1]-data[2][2])-data[0][1]*(pow(m,4)+pow(n,4)))
        Ey = 1/(pow(n,4)*data[0][0]+pow(m,2)*pow(n,2)*(data[2][2]+2*data[0][1])+pow(m,4)*data[1][1]) 
        Gxy = 1/(4*pow(m,2)*pow(n,2)*(data[0][0]+data[1][1]-2*data[0][1])+pow(pow(m,2)-pow(n,2),2)*data[2][2])
        etaxy_x = Ex*(pow(m,3)*n*(2*data[0][0]-2*data[0][1]-data[2][2])-pow(n,3)*m*(2*data[1][1]-2*data[0][1]-data[2][2]))
        etaxy_y = Ey*(pow(n,3)*m*(2*data[0][0]-2*data[0][1]-data[2][2])-pow(m,3)*n*(2*data[1][1]-2*data[0][1]-data[2][2]))
    
    if Material_properties == True:
        Ex = 1/(pow(m,4)/data[0]+pow(m,2)*pow(n,2)*(1/data[3]-(2*data[1])/data[0])+pow(n,4)/data[2])
        nuxy = -Ex*(-1*pow(m,2)*pow(n,2)*(1/data[0]+1/data[2]-1/data[3])+(data[1]*(pow(m,4)+pow(n,4)))/data[0])
        Ey = 1/(pow(n,4)/data[0]+pow(m,2)*pow(n,2)*(1/data[3]-(2*data[1])/data[0])+pow(m,4)/data[2])
        Gxy = 1/(4*pow(m,2)*pow(n,2)*(1/data[0]+1/data[2]+(2*data[1])/data[0])+(pow(pow(m,2)-pow(n,2),2))/data[3])
        etaxy_x = Ex*(pow(m,3)*n*(2/data[0]+(2*data[1])/data[0]-1/data[3])-pow(n,3)*m*(2/data[2]+(2*data[1])/data[0]-1/data[3]))
        etaxy_y = Ey*(pow(n,3)*m*(2/data[0]+(2*data[1])/data[0]-1/data[3])-pow(m,3)*n*(2/data[2]+(2*data[1])/data[0]-1/data[3]))
    return Ex,nuxy,Ey,Gxy,etaxy_x,etaxy_y

## Helper function 
def plot_properties_angle(data,angle):
    x = np.linspace(0,90,180)
    print(x.shape)
    Ex,nuxy,Ey,Gxy,etaxy_x,etaxy_y = effective_lamina_properties_angle(Material_properties=True,data=data,angle=x)
    print(Ex.shape,nuxy.shape,Ey.shape,Gxy.shape,etaxy_x.shape,etaxy_y.shape)
    fig = plt.figure(figsize=(40,20))
    #plt.plot(x,Ex,color='red',label='Ex')
    #plt.plot(x,Ey,color='blue',label='Ey')
    plt.plot(x,Gxy,color='green',label='Gxy')
    plt.plot(x,nuxy,color='yellow',label='nuxy')
    #plt.plot(x,etaxy_x,color='magneta',label='etaxy_x')
    plt.plot(x,etaxy_x,color='cyan',label='etaxy_y')
    plt.xlabel('Angle')
    plt.title('Lamina properties at Angle(theta)')
    Ex_ang,nuxy_ang,Ey_ang,Gxy_ang,etaxy_x_ang,etaxy_y_ang = effective_lamina_properties_angle(Material_properties=True,data=data,angle=angle) 
    #plt.plot(angle,Ex_ang,'b*')
    plt.plot(angle,nuxy_ang,'b*')
    #plt.plot(angle,Ey_ang,'b*')
    plt.plot(angle,Gxy_ang,'b*')
    #plt.plot(angle,etaxy_x_ang,'b*')
    #plt.plot(angle,etaxy_y_ang,'b*')
    plt.show()
    plt.legend(['Simple line'])
    return fig

def Stiffness_matrix_angle(data,angle):
    Q_planar_angle = np.zeros((3,3),dtype=float)
    m = cos(angle)
    n = sin(angle)
    Q_planar = stiffness_compliance_matrix(data[0],data[1]) ###(To be modified)
    Q_planar_angle[0][0] = pow(m,4)*Q_planar[0][0]+2*pow(m,2)*pow(n,2)*(Q_planar[0][1]+2*Q_planar[2][2])+pow(n,4)*Q_planar[1][1]
    Q_planar_angle[0][1] = pow(m,2)*pow(n,2)*(Q_planar[0][0]+Q_planar[1][1]-4*Q_planar[2][2])+Q_planar[0][1]*(pow(m,4)+pow(n,4))
    Q_planar_angle[0][2] = pow(m,3)*n*(Q_planar[0][0]-Q_planar[0][1]-2*Q_planar[2][2])+pow(n,3)*m*(Q_planar[0][1]-Q_planar[1][1]+2*Q_planar[2][2])
    Q_planar_angle[1][0] = Q_planar_angle[0][1]
    Q_planar_angle[1][1] = pow(n,4)*Q_planar[0][0]+2*pow(m,2)*pow(n,2)*(Q_planar[0][1]+2*Q_planar[2][2])+pow(m,4)*Q_planar[1][1]
    Q_planar_angle[1][2] = pow(n,3)*m*(Q_planar[0][0]-Q_planar[0][1]+2*Q_planar[2][2])-pow(n,3)*m*(Q_planar[0][1]-Q_planar[1][1]-2*Q_planar[2][2])
    Q_planar_angle[2][0] = Q_planar_angle[0][2]
    Q_planar_angle[2][1] = Q_planar_angle[1][2]
    Q_planar_angle[2][2] = pow(m,2)*pow(n,2)*(data[0][0]+data[1][1]-2*data[0][1])+pow(pow(m,2)-pow(n,2),2)*data[2][2]
    return Q_planar_angle


#### Sub routine 3 ####

##### Calculating A B D matrix for laminate ####
## Inputs - material properties of 0 deg lamina, lamina_sequence,lamina_thickness
## Outputs - A,B,D

def Laminate_parameters(data,laminate_sequence,lamina_thickness):
    z_sequence = []
    Q_matrices = []
    no_laminas = len(laminate_sequence)
    for i in range(no_laminas):
        Q_matrices.append(Stiffness_matrix_angle(data,laminate_sequence[i]))
    z_sequence.append(-(no_laminas/2)*lamina_thickness)
    for i in range(no_laminas):
        z_sequence.append(z_sequence[-1]+lamina_thickness)
    A = 0
    B = 0
    D = 0
    for i in range(no_laminas):
        A += Q_matrices[i] * (z_sequence[i+1]-z_sequence[i])
        B += Q_matrices[i] * (pow(z_sequence[i+1],2)-pow(z_sequence[i],2))
        D += Q_matrices[i] * (pow(z_sequence[i+1],3)-pow(z_sequence[i],3))
    B = B/2
    D = D/3
    z_laminas = []
    for i in range(no_laminas):
        z_laminas.append((z_sequence[i+1]+z_sequence[i])/2)
    return A,B,D,z_laminas,Q_matrices

#### Calculation of stress vectors for each lamina 
## Inputs - A,B,D matrix of laminate ,N(Normal traction),M(Bending moment)   
## Oututs - Stress lamina (3*1 vector) for each lamina

def stress_lamina(A,B,D,z_laminas,Q_matrices,N,M):
    laminate_matrix = np.block([[A,B],[B,D]])
    traction_bending_vector = np.transpose(np.array([N[0],N[1],N[2],M[0],M[1],M[2]]))
    strain_curvature_vector = np.dot(inv(laminate_matrix),traction_bending_vector)
    strain_laminas = []
    stress_laminas = []
    for i in range(len(z_laminas)):
        strain_laminas.append(strain_curvature_vector[:3]+z_laminas[i]*strain_curvature_vector[3:])
    for i in range(len(z_laminas)):
        stress_laminas.append(np.dot(Q_matrices[i],stress_laminas[i]))
    return stress_laminas

#### Sub routine 4 ####

### Implementation of Hashin Failure 2D
## Input - Stress Lamina, Strength of Lamina
## Output - True(if Failure occurs)/False(if Failure doesnt occurs)
def hashin_failure(stress_lamina,X,X_,Y,Y_,S):
    result = True
    ## Calculating for Fibre ##
    if stress_lamina[0]>0: #Tensile fibre failure
        if(pow(stress_lamina[0]/X,2)+pow(stress_lamina[2]/S,2)<1):
            result = result and False
        else:
            result = result and True
    else: #Compressive fibre failure
        if(pow(stress_lamina[0]/X_,2)<1):
            result = result and False
        else:
            result = result and True
    ## Calculating for Matrix ##
    if stress_lamina[1]>0: #Matrix Tensile Failure
        if(pow(stress_lamina[1]/Y,2)+pow(stress_lamina[3]/S,2)<1):
            result = result and False
        else:
            result = result and True
    else: #Matrix Compressive Failure
        if((pow(Y_/2*S,2)-1)*(stress_lamina[1]/Y_)+pow(stress_lamina[1]/4*S,2)+pow(stress_lamina[2]/S,2)<1):
            result = result and False
        else:
            result = result and True
    return result 

if __name__ == "__main__":
    ### My composite properties ###
    ## Fibre name - AS4 + Matrix name - BSL914c Epoxy ##
    ## (Fibre Details) E1_Fibre,E2_fibre,nu12_fibre,nu23_fibre,G12_fibre,G23_fibre,Volume_fraction_fibre,chamis_correction ###
    ## (Matrix Details )E_matrix,nu_matrix,G_matrix ##
    E1_fibre = 225
    E2_fibre = 15
    G12_fibre = 15
    nu12_fibre = 0.2
    nu23_fibre = 0.25 
    G23_fibre = E2_fibre/(2*(1+nu23_fibre))
    E_matrix = 4
    nu_matrix = 0.35
    G_matrix = E_matrix/(2*(1+nu_matrix))
    Volume_fraction_fibre = 0.516
    E1,E2,E3,nu12,nu13,nu23,G12,G13,G23 = effective_lamina_properties(E1_fibre,E2_fibre,nu12_fibre,nu23_fibre,G12_fibre,G23_fibre,E_matrix,nu_matrix,G_matrix,Volume_fraction_fibre)
    #print(E1,E2,E3,nu12,nu13,nu23,G12,G13,G23)
    Q_planar,S_planar = stiffness_compliance_matrix(E1,E2,E3,nu12,nu13,nu23,G12,G13,G23)
    #print(Q_planar,S_planar)
    #print(inv(Q_planar))
    #Ex,nuxy,Ey,Gxy,etaxy_x,etaxy_y = effective_lamina_properties_angle(Material_properties=True,data=[E1,nu12,E2,G12],angle=50)
    fig = plot_properties_angle([E1,nu12,E2,G12],20)

