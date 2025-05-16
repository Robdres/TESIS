import numpy as np

def bmatrix(a):
    """Returns a LaTeX bmatrix
    :a: numpy array
    :returns: LaTeX bmatrix as a string
    """
    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{bmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv +=  [r'\end{bmatrix}']
    return '\n'.join(rv)

def matrix(labels,a):
    """Returns a LaTeX bmatrix
    :a: numpy array
    :returns: LaTeX bmatrix as a string
    """
    values = []
    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{bmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv +=  [r'\end{bmatrix}']
    return '\n'.join(rv)

def diference(array):
    results = []
    labels = []
    data = array[:,1:]
    for i in range(len(array)):
        for j in range(i,len(array)):
            if(array[j][0] != array[i][0]):
                labels.append("O_"+str(int(i))+"O_"+str(int(j)))
                results.append(data[j]-data[i])
    results = np.array(results)
    return [labels,results]


A = np.array([[1,0.1,0.1,0.1,0.1,0.1,0.1], 
              [0,0.1,0.3,0.2,0.1,0.2,0.1],
              [1,0.1,0.5,0.3,0.1,0.1,0.2], 
              [0,0.2,0.7,0.4,0.1,0.1,0.3], 
              [1,0.3,0.9,0.5,0.2,0.2,0.4], 
              [0,0.4,0.1,0.6,0.3,0.1,0.5]])


labels,results = diference(A)

binary = []
results = np.absolute(results)
for i in results>0.2:
    binary.append(list(map(int,i)))
binary = np.array(binary)

print(bmatrix(results))
print(bmatrix(binary))
\begin{bmatrix}
  0. & 0.2 & 0.1 & 0. & 0.1 & 0.\\
  0.1 & 0.6 & 0.3 & 0. & 0. & 0.2\\
  0.3 & 0. & 0.5 & 0.2 & 0. & 0.4\\
  0. & 0.2 & 0.1 & 0. & 0.1 & 0.1\\
  0.2 & 0.6 & 0.3 & 0.1 & 0. & 0.3\\
  0.1 & 0.2 & 0.1 & 0. & 0. & 0.1\\
  0.3 & 0.4 & 0.3 & 0.2 & 0. & 0.3\\
  0.1 & 0.2 & 0.1 & 0.1 & 0.1 & 0.1\\
  0.1 & 0.8 & 0.1 & 0.1 & 0.1 & 0.1\\
\end{bmatrix}
\begin{bmatrix}
  0 & 0 & 0 & 0 & 0 & 0\\
  0 & 1 & 1 & 0 & 0 & 0\\
  1 & 0 & 1 & 0 & 0 & 1\\
  0 & 0 & 0 & 0 & 0 & 0\\
  0 & 1 & 1 & 0 & 0 & 1\\
  0 & 0 & 0 & 0 & 0 & 0\\
  1 & 1 & 1 & 0 & 0 & 1\\
  0 & 1 & 0 & 0 & 0 & 0\\
  0 & 1 & 0 & 0 & 0 & 0\\
\end{bmatrix}
