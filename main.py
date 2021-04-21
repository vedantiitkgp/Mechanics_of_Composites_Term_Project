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
    E1,E2,E3,nu12,nu13,nu23,G12,G13,G23 = round(E1,3),round(E2,3),round(E3,3),round(nu12,3),round(nu13,3),round(nu23,3),round(G12,3),round(G13,3),round(G23,3)
    return E1,E2,E3,nu12,nu13,nu23,G12,G13,G23

#### Sub routine 2 ####

##### Calculating S and Q matrix for lamina ####
## Inputs -E1,E2,E3,nu12,nu13,nu23,G12,G13,G23
## Outputs - Q(3x3 Matrix), S(3x3 Matrix)   

def stiffness_compliance_matrix(E1=0,E2=0,E3=0,nu12=0,nu13=0,nu23=0,G12=0,G13=0,G23=0):
    S_matrix = np.zeros((6,6),dtype=float)
    if(E1!=0): 
        S_matrix[0][0] = 1/E1
        S_matrix[0][1] = (-1*nu12)/E1
        S_matrix[0][2] = (-1*nu13)/E1
    S_matrix[1][0] = S_matrix[0][1] 
    if(E2!=0): S_matrix[1][1] = 1/E2
    if(E1!=0): S_matrix[1][2] = (-1*nu23)/E1
    S_matrix[2][0] = S_matrix[0][2]
    S_matrix[2][1] = S_matrix[1][2]
    if(E3!=0): S_matrix[2][2] = 1/E3
    if(G23!=0): S_matrix[3][3] = 1/G23
    if(G13!=0): S_matrix[4][4] = 1/G13
    if(G12!=0): S_matrix[5][5] = 1/G12

    nu21 = (nu12 * E2)/E1
    nu31 = (nu13 * E3)/E1
    nu32 = (nu23 * E3)/E2
    try:
        Q_matrix = inv(S_matrix)
    except:
        pass

    S_planar = np.zeros((3,3),dtype=float)
    S_planar[0][0] = S_matrix[0][0]
    S_planar[0][1] = S_matrix[0][1]
    S_planar[1][0] = S_matrix[1][0]
    S_planar[1][1] = S_matrix[1][1]
    S_planar[2][2] = S_matrix[5][5]
    Q_planar = inv(S_planar)
    Q_planar,S_planar = np.around(Q_planar,decimals = 3),np.around(S_planar,decimals = 3)
    return Q_planar,S_planar

#### Calculate the modulus and elastic propties at another angle ####
## Inputs - Q_matrix(3X3 Matrix)/S_matrix(3X3 Matrix)/Material_Properties([E1,nu12,E2,G12])
## Outputs - Ex,nuxy,Ey,Gxy,etaxy_x,etaxy_y
def effective_lamina_properties_angle(Q_matrix=False,S_matrix=False,Material_properties=False,data=1,angle=0):
    m = np.cos(np.deg2rad(angle))
    n = np.sin(np.deg2rad(angle))
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
        nuxy = Ex*(-1*pow(m,2)*pow(n,2)*(1/data[0]+1/data[2]-1/data[3])+(data[1]*(pow(m,4)+pow(n,4)))/data[0])
        Ey = 1/(pow(n,4)/data[0]+pow(m,2)*pow(n,2)*(1/data[3]-(2*data[1])/data[0])+pow(m,4)/data[2])
        Gxy = 1/(4*pow(m,2)*pow(n,2)*(1/data[0]+1/data[2]+(2*data[1])/data[0])+(pow(pow(m,2)-pow(n,2),2))/data[3])
        etaxy_x = abs(Ex*(pow(m,3)*n*(2/data[0]+(2*data[1])/data[0]-1/data[3])-pow(n,3)*m*(2/data[2]+(2*data[1])/data[0]-1/data[3])))
        etaxy_y = abs(Ey*(pow(n,3)*m*(2/data[0]+(2*data[1])/data[0]-1/data[3])-pow(m,3)*n*(2/data[2]+(2*data[1])/data[0]-1/data[3])))
    try:
        Ex,nuxy,Ey,Gxy,etaxy_x,etaxy_y = round(Ex,3),round(nuxy,3),round(Ey,3),round(Gxy,3),round(etaxy_x,3),round(etaxy_y,3)
    except:
        Ex,nuxy,Ey,Gxy,etaxy_x,etaxy_y = np.around(Ex,3),np.round(nuxy,3),np.around(Ey,3),np.around(Gxy,3),np.around(etaxy_x,3),np.around(etaxy_y,3)
    return Ex,nuxy,Ey,Gxy,etaxy_x,etaxy_y

## Helper function 
def plot_properties_angle(data,angle=0):
    x = np.linspace(0,90,90)
    Ex,nuxy,Ey,Gxy,etaxy_x,etaxy_y = effective_lamina_properties_angle(Material_properties=True,data=data,angle=x)
    fig, axs = plt.subplots(3, 2)
    fig.suptitle('Laminate properties with Angle(theta)',fontsize='xx-large',fontweight='bold')
    axs[0,0].plot(x,Ex,color='red',label='Ex')
    axs[0,0].set_title('Ex v/s angle')
    axs[0,0].grid(color = 'green', linestyle = '--', linewidth = 0.4)
    axs[0,0].legend()
    axs[0,0].set(ylabel='Stress(GPa)')
    axs[0,1].plot(x,Ey,color='blue',label='Ey')
    axs[0,1].set_title('Ey v/s angle')
    axs[0,1].grid(color = 'green', linestyle = '--', linewidth = 0.4)
    axs[0,1].legend()
    axs[0,1].set(ylabel='Stress(GPa)')
    axs[1,0].plot(x,Gxy,color='green',label='Gxy')
    axs[1,0].set_title('Gxy v/s angle')
    axs[1,0].grid(color = 'green', linestyle = '--', linewidth = 0.4)
    axs[1,0].legend()
    axs[1,0].set(ylabel='Stress(GPa)')
    axs[1,1].plot(x,nuxy,color='orange',label='nuxy')
    axs[1,1].set_title('nuxy v/s angle')
    axs[1,1].grid(color = 'green', linestyle = '--', linewidth = 0.4)
    axs[1,1].legend()
    axs[1,1].set(ylabel='Poisson ratio')
    axs[2,0].plot(x,etaxy_x,color='magenta',label='etaxy-x')
    axs[2,0].set_title('etaxy-x v/s angle')
    axs[2,0].grid(color = 'green', linestyle = '--', linewidth = 0.4)
    axs[2,0].legend()
    axs[2,0].set(xlabel='angle(degrees)',ylabel='shear coupling ratio')
    axs[2,1].plot(x,etaxy_y,color='cyan',label='etaxy-y')
    axs[2,1].set_title('etaxy-y v/s angle')
    axs[2,1].grid(color = 'green', linestyle = '--', linewidth = 0.4)
    axs[2,1].legend()
    axs[2,1].set(xlabel='angle(degrees)',ylabel='shear coupling ratio')
    '''
    for ax in fig.get_axes():
        ax.label_outer()
    '''
    Ex_ang,nuxy_ang,Ey_ang,Gxy_ang,etaxy_x_ang,etaxy_y_ang = effective_lamina_properties_angle(Material_properties=True,data=data,angle=angle) 
    axs[0,0].plot(angle,Ex_ang,'bo')
    axs[0,1].plot(angle,Ey_ang,'bo')
    axs[1,0].plot(angle,Gxy_ang,'bo')
    axs[1,1].plot(angle,nuxy_ang,'bo')
    axs[2,0].plot(angle,etaxy_x_ang,'bo')
    axs[2,1].plot(angle,etaxy_y_ang,'bo')
    plt.show()
    fig.savefig('lamina_variation_angle.jpg')
    return fig

#### Calculate of Stiffness Matrix at angle ####
## Inputs - Material_Propties([E1,nu12,E2,G12]),Angle
## Outputs - Q_planar_angle
def Stiffness_matrix_angle(data,angle):
    Q_planar_angle = np.zeros((3,3),dtype=float)
    m = np.cos(np.deg2rad(angle))
    n = np.sin(np.deg2rad(angle))
    Q_planar,S_planar = stiffness_compliance_matrix(E1=data[0],E2=data[2],nu12=data[1],G12=data[3])
    Q_planar_angle[0][0] = pow(m,4)*Q_planar[0][0]+2*pow(m,2)*pow(n,2)*(Q_planar[0][1]+2*Q_planar[2][2])+pow(n,4)*Q_planar[1][1]
    Q_planar_angle[0][1] = pow(m,2)*pow(n,2)*(Q_planar[0][0]+Q_planar[1][1]-4*Q_planar[2][2])+Q_planar[0][1]*(pow(m,4)+pow(n,4))
    Q_planar_angle[0][2] = pow(m,3)*n*(Q_planar[0][0]-Q_planar[0][1]-2*Q_planar[2][2])+pow(n,3)*m*(Q_planar[0][1]-Q_planar[1][1]+2*Q_planar[2][2])
    Q_planar_angle[1][0] = Q_planar_angle[0][1]
    Q_planar_angle[1][1] = pow(n,4)*Q_planar[0][0]+2*pow(m,2)*pow(n,2)*(Q_planar[0][1]+2*Q_planar[2][2])+pow(m,4)*Q_planar[1][1]
    Q_planar_angle[1][2] = pow(n,3)*m*(Q_planar[0][0]-Q_planar[0][1]+2*Q_planar[2][2])-pow(n,3)*m*(Q_planar[0][1]-Q_planar[1][1]-2*Q_planar[2][2])
    Q_planar_angle[2][0] = Q_planar_angle[0][2]
    Q_planar_angle[2][1] = Q_planar_angle[1][2]
    Q_planar_angle[2][2] = pow(m,2)*pow(n,2)*(Q_planar[0][0]+Q_planar[1][1]-2*Q_planar[0][1])+pow(pow(m,2)-pow(n,2),2)*Q_planar[2][2]
    Q_planar_angle = np.around(Q_planar_angle,decimals=3)
    return Q_planar_angle


#### Sub routine 3 ####

##### Calculating A B D matrix for laminate ####
## Inputs - material properties of 0 deg lamina, lamina_sequence,lamina_thickness
## Outputs - A,B,D

def Laminate_parameters(data,laminate_sequence,lamina_thickness=1000):
    z_sequence = []
    Q_matrices = []
    no_laminas = len(laminate_sequence)
    lamina_thickness = lamina_thickness/no_laminas
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
    A,B,D = np.around(A,decimals=3),np.around(B,decimals=3),np.around(D,decimals=3)
    return A,B,D,z_laminas,Q_matrices,laminate_sequence

#### Calculation of stress vectors for each lamina 
## Inputs - A,B,D matrix of laminate ,N(Normal traction),M(Bending moment)   
## Oututs - Stress lamina (3*1 vector) for each lamina

def stress_lamina(A,B,D,z_laminas,Q_matrices,laminate_sequence,N,M):
    laminate_matrix = np.block([[A,B],[B,D]])
    traction_bending_vector = np.transpose(np.array([N[0],N[1],N[2],M[0],M[1],M[2]]))
    strain_curvature_vector = np.dot(inv(laminate_matrix),traction_bending_vector)
    print(strain_curvature_vector)
    strain_laminas = []
    stress_laminas = []
    for i in range(len(z_laminas)):
        strain_laminas.append(strain_curvature_vector[:3]+z_laminas[i]*strain_curvature_vector[3:])
    for i in range(len(z_laminas)):
        stress_laminas.append(angle_correction(np.dot(Q_matrices[i],strain_laminas[i]),laminate_sequence[i]))
    return stress_laminas

#Helper Function
def angle_correction(stress_xy,angle):
    m = np.cos(np.deg2rad(angle))
    n = np.sin(np.deg2rad(angle))
    T = np.zeros((3,3),dtype=float)
    T[0][0] = pow(m,2)
    T[0][1] = pow(n,2)
    T[0][2] = 2*m*n
    T[1][0] = pow(n,2)
    T[1][1] = pow(m,2)
    T[1][2] = -2*m*n
    T[2][0] = -m*n
    T[2][1] = m*n
    T[2][2] = pow(m,2)-pow(n,2)
    stress_12 = np.dot(T,stress_xy)
    return stress_12



#### Sub routine 4 ####

### Implementation of Hashin Failure 2D
## Input - Stress Lamina, Strength of Lamina
## Output - True(if Failure occurs)/False(if Failure doesnt occurs)
def hashin_failure(stress_lamina,X,X_,Y,Y_,S):
    result = True
    safety_factor = 2
    ## Calculating for Fibre ##
    if stress_lamina[0]>0: #Tensile fibre failure
        if(pow(stress_lamina[0]/X,2)+pow(stress_lamina[2]/S,2)<1):
            result = result and False
        else:
            result = result and True
        safety_factor = quadratic_solver_safety(pow(stress_lamina[0]/X,2)+pow(stress_lamina[2]/S,2),0,-1)
    else: #Compressive fibre failure
        if(pow(stress_lamina[0]/X_,2)<1):
            result = result and False
        else:
            result = result and True
        safety_factor = quadratic_solver_safety(pow(stress_lamina[0]/X_,2),0,-1)
    ## Calculating for Matrix ##
    if stress_lamina[1]>0: #Matrix Tensile Failure
        if(pow(stress_lamina[1]/Y,2)+pow(stress_lamina[2]/S,2)<1):
            result = result and False
        else:
            result = result and True
        safety_factor = min(safety_factor,quadratic_solver_safety(pow(stress_lamina[1]/Y,2)+pow(stress_lamina[2]/S,2),0,-1))
    else: #Matrix Compressive Failure
        if((pow(Y_/2*S,2)-1)*(stress_lamina[1]/Y_)+pow(stress_lamina[1]/4*S,2)+pow(stress_lamina[2]/S,2)<1):
            result = result and False
        else:
            result = result and True
        safety_factor = min(safety_factor,quadratic_solver_safety(pow(stress_lamina[1]/4*S,2)+pow(stress_lamina[2]/S,2),(pow(Y_/2*S,2)-1)*(stress_lamina[1]/Y_),-1))
    safety_factor = round(safety_factor,3)
    return result,safety_factor 

## Helper function ##
def quadratic_solver_safety(a,b,c):
    # calculate the discriminant
    d = (b**2) - (4*a*c)

    # find two solutions
    sol1 = (-b-sqrt(d))/(2*a)
    sol2 = (-b+sqrt(d))/(2*a)
    if(sol1>0 and sol2>0):
        return min(sol1,sol2)
    elif(sol1>0 or sol2>0):
        if(sol1>0): return sol1
        else: return sol2
    else:
        raise Exception("Quadratic coeffecients give illegal answers")



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
    #print(G23_fibre,G_matrix)
    Q_planar,S_planar = stiffness_compliance_matrix(E1,E2,E3,nu12,nu13,nu23,G12,G13,G23)
    #print(Q_planar,S_planar)
    #Ex,nuxy,Ey,Gxy,etaxy_x,etaxy_y = effective_lamina_properties_angle(Material_properties=True,data=[E1,nu12,E2,G12],angle=50)
    #fig = plot_properties_angle([E1,nu12,E2,G12],20)
    #Q_planar_angle = Stiffness_matrix_angle(data=[E1,nu12,E2,G12],angle=90)
    #print(Q_planar_angle)
    A,B,D,z_laminas,Q_matrices,laminate_seq = Laminate_parameters(data=[E1,nu12,E2,G12],laminate_sequence=[0,29,-29,90,90,-29,29,0],lamina_thickness=1000)
    print(D)
    #print(A,B,D,z_laminas,Q_matrices)
    #print(D)
    stress_laminas = stress_lamina(A,B,D,z_laminas,Q_matrices,laminate_seq,N=[100000,0,0],M=[0,0,0])
    #print(stress_laminas[0])
    result,safety_factor = hashin_failure(stress_laminas[0],X=1550,X_=1550,Y=150,Y_=220,S=93)
    #print(result,safety_factor)

