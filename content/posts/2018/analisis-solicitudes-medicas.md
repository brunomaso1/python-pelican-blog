Title: ANÁLISIS DE LAS SOLICITUDES MEDICAS URUGUAY 2016
Date: 2019-12-29 12:00
Modified: 2018-12-29 12:00
Category: Ciencia de datos
Tags: CRISP-DM, Aprendizaje automático, Rapidminer, Minería de datos, Inteligencia artificial, Programación, Solicitudes2018, Uruguay, Aprendizaje supervisado
Slug: analisis-solicitudes-medicas
Summary: Análisis de las solicitudes medicas de Uruguay del año 2016.
JavaScripts: tocConverter.js
Status: published

[TOC]

## Entendimiento del negocio
---

<center><small><a href="https://catalogodatos.gub.uy/dataset/solicitudes_2016_fondo-nacional-de-recursos">https://catalogodatos.gub.uy/dataset/solicitudes_2016_fondo-nacional-de-recursos</a></small></center>

<div style="text-align:center"><img src="http://www.fnr.gub.uy/sites/all/themes/fnrpb2013/logo.png" alt="drawing" width="60%" height="60%"/></div><br/>

El **Fondo Nacional de Recursos** (FNR) es una institución creada por el decreto *Ley 14.897* con carácter de persona pública no estatal, que brinda cobertura financiera a procedimientos de medicina altamente especializada y a medicamentos de alto precio para toda la población que se radique en el país y que sea usuaria del Sistema Nacional Integrado de Salud.

En el caso de los procedimientos cubiertos estos se efectúan a través de los Institutos de Medicina Altamente Especializada (IMAE) que son prestadores públicos o privados, que cuentan con la habilitación del Ministerio de Salud Pública para su realización.

### Contexto

Actualmente, los medicamentos y actos médicos (de alto costo) necesitan una aprobación previa del FNR para su realización, por lo que cada caso es evaluado para luego tomar una decisión si brindar el apoyo económico o no.

<div style="text-align:center"><img src="https://fee.org/media/24118/health-care_mini.jpg?anchor=center&mode=crop&width=1920&rnd=131497055300000000" alt="drawing" width="90%" height="90%"/></div><br/>

### DataSet

El conjunto se puede obtener del siguiente link: [Datos](https://catalogodatos.gub.uy/dataset/28b09caf-a138-4942-a597-6c2d0d48c361/resource/ff334d61-a6de-40fe-b663-1cb239443f3c/download/datossolicitudes-2016.csv)

El dataset contiene información de las solicitudes (en Uruguay) de medicamentos de alto costo realizadas al FNR en el año 2016. Este dataset pertenece al gobierno uruguayo y en conjunto con AGESIC (Agencia de Gobierno electrónico y Sociedad de la Información y del Conocimiento) lo han publicado en su página de datos abiertos.

### Objetivo

El objetivo en este caso, es predecir si una solicitud de un paciente será APROVADA o NO APROVADA.

En el ámbito de Machine Learning este es un problema supervisado de clasificación binaria.

## Entendimiento de los datos
---

Antes de comenzar con el análisis y modelado de la solución del problema, debemos entender que explican los atributos.
En este punto se comprenden los atributos y se analiza su importancia para el problema y la solución.

### Atributos

Según los [metadatos](https://catalogodatos.gub.uy/dataset/28b09caf-a138-4942-a597-6c2d0d48c361/resource/41f9b26b-4ecc-4802-b0e9-54c6d9f3c2ab/download/metadatosjsonoutput.json) del dataset, el conjunto cuenta con 16 atributos (incluido la variable objetivo o label).

Los atributos y su descripción son:

- ```tipo_prestacion```: Tipo de prestación $\rightarrow$ *Tipo:* <span style="color:orange">**BINOMIAL** ("Acto Médico"; "Inicio de Tratamiento con medicamentos")</span>
- ```area```: Área de la prestación $\rightarrow$ *Tipo:* <span style="color:orange">**POLINOMIAL** ("MAC CARDIOLOGÍA"; ACTOS NEFROLOGÍA"; ...)</span>
- ```prestacion_cod```: Código de la prestación $\rightarrow$ *Tipo:* <span style="color:orange">**POLINOMIAL** ("101"; "1201"; ...)</span>
- ```prestacion_desc```: Descripción de la prestación $\rightarrow$ *Tipo:* <span style="color:orange">**POLINOMIAL** ("Protesis de rodilla - Implante"; "Cirugía cardíaca adultos"; ...)</span>
- ```fecha_solicitud```: Fecha de solicitud (Date) $\rightarrow$ *Tipo:* <span style="color:orange">**POLINOMIAL** ("08-11-2016"; "05-08-2016"; ...)</span>
- ```estado_solicitud```: Estado de la solicitud (String) $\rightarrow$ *Tipo:* <span style="color:orange">**BINOMIAL** ("AUTORIZADO"; "NO AUTORIZADO")</span>
- ```fecha_autorizacion```: Fecha de autorización (Date) $\rightarrow$ *Tipo:* <span style="color:orange">**POLINOMIAL** ("08-11-2016"; "05-08-2016"; ...)</span>
- ```Paciente```: Número de paciente (Integer) $\rightarrow$ *Tipo:* <span style="color:orange">**ENTERO**</span>
- ```Edad_años```: Edad en años (Integer) $\rightarrow$ *Tipo:* <span style="color:orange">**ENTERO**</span>
- ```Sexo```: Sexo (String) $\rightarrow$ *Tipo:* <span style="color:orange">**BINOMIAL** ("M"; "F")</span>
- ```Departamento_residencia```: Departamento de residencia del paciente (String) $\rightarrow$ *Tipo:* <span style="color:orange">**POLINOMIAL** ("MONTEVIDEO"; "FLORES"; ...)</span>
- ```prestador_salud```: Prestador de salud (String) $\rightarrow$ *Tipo:* <span style="color:orange">**POLINOMIAL** ("CASMU"; "COSEM"; ...)</span>
- ```prestador_departamento```: Departamento del prestador de salud (String) $\rightarrow$ *Tipo:* <span style="color:orange">**POLINOMIAL** ("MONTEVIDEO"; "FLORES"; ...)</span>
- ```prestador_tipo```: Tipo de prestador (String) $\rightarrow$ *Tipo:* <span style="color:orange">**POLINOMIAL** ("OTRO"; "IMAC"; ...)</span> 
- ```medico_solicitante```: Médico solicitante (String) $\rightarrow$ *Tipo:* <span style="color:orange">**POLINOMIAL** ("TOMAS DIESTE FRIEDHEIN"; "BRUNO MASOLLER"; ...)</span>
- ```imae```: IMAE (String) $\rightarrow$ *Tipo:* <span style="color:orange">**POLINOMIAL** ("COMEF"; "CAMOC"; ...)</span>

### Análisis de los atributos

En esta sección se hace un análisis previo de los atributos.

#### Importancia

La importancia de los atributos con respecto al contexto es muy importante, ya que atributos que no tienen importancia dado el contexto, pueden afectar la predicción final.

- ```tipo_prestacion``` $\Rightarrow$ El tipo de prestación es un dato importante ya que indica si es un acto médico o un medicamento. <span style="color:green">IMPORTANTE</span>
- ```area``` $\Rightarrow$ El área de prestación es importante, ya que indica el tipo de tratamiento que se ha realizado. <span style="color:green">IMPORTANTE</span>
- ```prestacion_cod``` $\Rightarrow$ El código de prestación es el tipo de tratamiento. <span style="color:green">IMPORTANTE</span>
- ```prestacion_desc``` $\Rightarrow$ Es la descripción de la presentación. Es el mismo atributo que prestacion_cod. <span style="color:red">NO IMPORTANTE</span>
- ```fecha_solicitud``` $\Rightarrow$ Es la fecha de la solicitud, como no estamos tomando en cuenta el tiempo, para este problema no es importante este atributo. <span style="color:red">NO IMPORTANTE</span>
- ```estado_solicitud``` $\Rightarrow$ Es la variable objetivo a predecir en este problema. <span style="color:violet">**IMPORTANTE**</span>
- ```fecha_autorizacion``` $\Rightarrow$ Es la fecha de la autorización, como no estamos tomando en cuenta el tiempo, para este problema no es importante este atributo. <span style="color:red">NO IMPORTANTE</span>
- ```Paciente``` $\Rightarrow$ En este caso, el numero de paciente lo tratamos como un identificador, por lo que para el entrenamiento no es importante. <span style="color:blue">IDENTIFICADOR</span>
- ```Edad_años``` $\Rightarrow$ La edad es importante para este problema. <span style="color:green">IMPORTANTE</span>
- ```Sexo``` $\Rightarrow$ ¿Será importante el sexo para decir si autorizar una solicitud? ¿Habrá discriminación de género? XD. <span style="color:green">IMPORTANTE</span>
- ```Departamento_residencia``` $\Rightarrow$ ¿Será importante el departamento de residencia para decir si autorizar una solicitud?. <span style="color:green">IMPORTANTE</span>
- ```prestador_salud``` $\Rightarrow$ Es importante porque este atributo dice de donde viene la solicitud. <span style="color:green">IMPORTANTE</span>
- ```prestador_departamento``` $\Rightarrow$ Es importante porque este atributo dice de que departamento viene la solicitud, lo que no es lo mismo que el departamento de residencia del paciente, aunque pueden estar altamente correlacionados. <span style="color:green">IMPORTANTE</span>
- ```prestador_tipo``` $\Rightarrow$ El tipo de prestador importa, porque no son los mismos las solicitudes privadas que las solicitudes de prestadores públicos. <span style="color:green">IMPORTANTE</span>
- ```medico_solicitante``` $\Rightarrow$ Puede ser que el medico sea importante. <span style="color:green">IMPORTANTE</span>
- ```imae``` $\Rightarrow$ Depende del FNR. <span style="color:green">IMPORTANTE</span>

## Preparación de los datos

En esta sección se preparan los datos para ser utilizados por varios modelos. Se tiene en cuenta las restricciones de los modelos, por lo que se pueden preparar varios conjuntos para distintos modelos.

Los problemas de este tipo se suelen utilizar modelos que resuelven problemas de clasificación binaria. Los modelos a probar son los siguientes:

- **Algoritmos lineales**:
	- *[Logistic Regression](https://en.wikipedia.org/wiki/Logistic_regression)*
		- Restricciones:
			1. Variable de salida binaria.
			2. Remover el ruido.
			3. Distribución gaussiana de los atributos.
			4. Remover atributos correlacionados.
	- *[Linear Discriminant Analysis](https://en.wikipedia.org/wiki/Linear_discriminant_analysis)*
		- Restricciones:
			1. Variable de salida categórica.
			2. Distribución gaussiana de los atributos.
			3. Remover los outliers.
			4. Misma varianza (estandarizar los datos).
			5. Atributos numéricos.
			
- **Algoritmos no lineales**:
	- *[CART](https://en.wikipedia.org/wiki/Decision_tree_learning)*
		- Restricciones:
			1. Sin restricciones.
	- *[Naive Bayes](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)*
		- Restricciones:
			1. Entradas categóricas.
			2. Distribuciones gausianas (para el caso de entradas continuas), se puede utilizar transformaciones o otro kernel.
			3. Variable de salida categórica.
			4. Transformación logarítmica de los datos.
	- *[KNN](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)*
		- Restricciones:
			1. Re-escalar los datos (normalizar).
			2. Tratamiento de atributos faltantes.
			3. Baja dimensionalidad (se beneficia altamente de poca dimensionalidad, puede ser una opción probar feature selección con este modelo).
	- *[SVM](https://en.wikipedia.org/wiki/Support_vector_machine)*
		- Restricciones:
			1. Atributos numéricos.
	- *[Redes neuronales](https://en.wikipedia.org/wiki/Neural_network)*
		- Restricciones:
			1. Atributos numéricos.

- **Ensambles**:
	- *[Random Forest](https://es.wikipedia.org/wiki/Random_forest)*
		- Restricciones:
			1. Sin restricciones.
	- *[Gradient Boosting Trees](https://en.wikipedia.org/wiki/Gradient_boosting)*
		- Restricciones:
			1. Sin restricciones.

### Importación de librerías

<div style="text-align:center"><img src="https://1xltkxylmzx3z8gd647akcdvov-wpengine.netdna-ssl.com/wp-content/uploads/2016/06/rapidminer-logo-retina.png" alt="drawing" width="60%" height="60%"/></div><br/>

En este caso, no se importan librerías ya que se usa [Rapidminer](https://rapidminer.com/).

### Importación de los datos

Importamos el conjunto dentro de rapidminer (mediante la opción "Import Data"):

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-1.png" alt="drawing" width="80%" height="80%"/></div><br/>

Una vez que importamos los datos en rapidminer, seleccionamos el identificador de persona como ID y el atributo *estado_solicitud* como label utilizando el operador ```Set Role```:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-2.png" alt="drawing" width="50%" height="50%"/></div><br/>

Podemos ver, luego que ejecutamos que rapidminer nos identifica el ID y label:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-3.png" alt="drawing" width="80%" height="80%"/></div><br/>

En este punto también filtramos los atributos que analizamos anteriormente y detectamos (con el conocimiento del negocio actual) que no soy relevantes para el problema en cuestión. Para esto utilizamos el operador ```Select Attributes```. 
Estos atributos son:

- *fecha_solicitud*
- *fecha_autorizacion*
- *prestacion_desc*

Para realizar esto en rapidminer, seleccionamos los atributos en las propiedades del operador y luego seleccionamos la propiedad de "invert selection" para que nos deje solo el resto de los atributos:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-4.png" alt="drawing" width="80%" height="80%"/></div><br/>

### Visualización de los datos

Podemos visualizar los datos una vez que ejecutamos el proceso:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-6.png" alt="drawing" width="80%" height="80%"/></div><br/>

Como resultado podemos ver que se tienen 24138 datos con atributos del tipo:

- Enteros $\rightarrow$ 2 (3 si contamos el identificador).
- Nominales $\rightarrow$  11 (12 si contamos la variable dependiente).

Para visualizar los datos utilizamos la pestaña "Statistics" de rapidminer que nos brinda resúmenes de los datos:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-5.png" alt="drawing" width="80%" height="80%"/></div><br/>

### Tratamiento de los datos

En este punto se realizan las transformaciones de los datos que se adecuan a los modelos a utilizar.

#### Sanitizar los datos

La sanitización de los datos se utiliza ya que pueden haber instancias que estén mal, en relación al tipo de dato. Este análisis es más a nivel de negocio que de dato, ya que el negocio implica reglas que los datos deben cumplir.
Primeramente, podemos observar que el atributo *Sexo* tiene una clase "U". Esta clase no debería existir, ya que estamos hablando solamente de mujeres ("F") y hombres ("M"). No estamos teniendo en cuenta los que no se han definido todavía ("U"). Por lo tanto, declaramos esta clase como un valor faltante, para luego ser tratada. 
Lo mismo pasa con el atributo *prestador_departamento*, la clase "SIN DATO" la tomamos como un dato faltante.

Para declarar estos datos como faltantes, utilizamos el operador ```Declare Missing Value```:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-7.png" alt="drawing" width="80%" height="80%"/></div><br/>

En este caso, podemos ver que el atributo *prestacion_cod* debemos re-declararlo como nominal, ya que es nuestra definición del negocio. Para esto utilizamos el operador ```Numerical to Polynominal```, y seleccionamos el atributo en cuestión:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-8.png" alt="drawing" width="80%" height="80%"/></div><br/>

Nota (atributos duplicados): En este caso no hay atributos duplicados, ya que cada paciente es distinto, por lo que pueden haber solicitudes iguales pero pacientes distintos.

#### Tratamiento datos faltantes

Los datos faltantes son inadmisibles para muchos modelos. El tratamiento de los datos faltantes implica imputar un valor, eliminar dichos datos o eliminar el atributo.

El atributo *medico_solicitante* tiene muchos faltantes, pero estos faltantes nos importan, ya que son los casos en donde no hubo un medico involucrado en realizar la solicitud. Es por esto, que imputamos estos atributos faltantes con una nueva clase "SIN MEDICO" para así tener una comprensión de que pasa con las solicitudes que no tienen un médico como solicitante. Esta operación la realizamos con el operador ```Replace Missing Values```:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-9.png" alt="drawing" width="80%" height="80%"/></div><br/>

Esta acción nos ha generado una nueva clase que como podemos observar es la mayor, lo que implica que la mayor cantidad de solicitudes se envían sin un médico solicitante. Luego podremos ver si es importante o no el médico solicitante:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-10.png" alt="drawing" width="80%" height="80%"/></div><br/>

Para el resto de los datos, como son pocos, simplemente filtramos los atributos que no tienen datos faltantes mediante el operador ```Filter examples```:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-11.png" alt="drawing" width="80%" height="80%"/></div><br/>

Luego de filtrado los atributos faltantes, nos quedan **24135** datos (luego de los tratamientos, habían unicamente 3 faltantes).

#### Tratamiento de outliers

Hay muchos modelos en los cuales los outliers reducen la performance o inducen un sesgo indeseado. Por eso, se debe detectar y tratar los outliers para evitar este tipo de problemas.

En este caso, ya hemos filtrado outliers que se sospecha que han sido mal ingresados por el sistema, sin embargo, un paso futuro sería aplicar algún algoritmo de detección de outliers para datos categóricos (como por ejemplo HBOS).

#### Correlación de atributos

Hay muchos (como los modelos lineales) que la correlación de los atributos influye fuertemente en los modelos. Es por esto, que muchas veces se debe chequear la correlación de los atributos para así eliminar los que están altamente correlacionados. Previamente, convertimos los valores a numéricos utilizando un en codeado simple (asigna a cada clase un número entero). Para esto utilizamos el operador ```Nominal to Numerical```:


<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-12.png" alt="drawing" width="80%" height="80%"/></div><br/>

El resultado nos quedaría:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-13.png" alt="drawing" width="80%" height="80%"/></div><br/>

Para calcular la matriz de correlación utilizamos el operador ```Correlation Matrix```:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-14.png" alt="drawing" width="80%" height="80%"/></div><br/>

Una vez que ejecutamos, obtenemos la siguiente matriz de correlación:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-15.png" alt="drawing" width="80%" height="80%"/></div><br/>

Si seleccionamos las correlaciones mayores al 0.5, tenemos las siguientes:

- prestacion_cod vs area $\rightarrow$ 0.94934017096856
- prestacion_cod vs imae $\rightarrow$ 0.8779232011993128
- area vs imae $\rightarrow$ 0.8523444883137807
- medico_solicitante vs prestacion_cod $\rightarrow$ 0.8311839275581686
- tipo_prestacion vs area $\rightarrow$ 0.8169807912406536
- tipo_prestacion vs imae $\rightarrow$ 0.7981221562193258
- prestacion_cod vs tipo_prestacion $\rightarrow$ 0.7807664805402255
- medico_solicitante vs imae $\rightarrow$ 0.7602177011564148

En este punto podemos ver que hay varias relaciones, que desde el negocio tienen lógica, por ejemplo, el atributo *prestacion_cod* está altamente relacionado con el atributo *área*, ya que cada prestación (acto médico o medicamento) pertenece únicamente a un área:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-16.png" alt="drawing" width="80%" height="80%"/></div><br/>

En este sentido, podemos eliminar el atributo *area* (prestacion_cod nos brinda información más detallada sobre el problema). Vamos a dividir el conjunto en los datos filtrados por la correlación y los datos no filtrados.

Podemos realizar la misma suposición con respecto a los otros atributos (de un modo u otro, *area*, *imae*, *tipo_prestacion* y *medico_solicitante* son generalizaciones de *prestacion_cod*).

Por lo tanto, un conjunto tiene todos los atributos luego de la preparación de los datos y el otro tiene los siguientes atributos filtrados:

- *area*
- *imae*
- *medico_solicitante*
- *tipo_prestacion*

#### Feature extraction

Muchas veces se puede "diseñar" un atributo que es combinación de otros atributos (lineal o no lineal) para así obtener más información. Tal vez, este atributo generado es un mejor predictor y se mejora la solución.

En este caso no se ve a simple vista algún nuevo atributo que se pueda generar y que pueda mejorar la predicción.

#### Transformaciones de los datos

En este punto se realizan las transformaciones necesarias de los datos. Las transformaciones incluyen desde transformaciones para reducir el sesgo o ajustar distribuciones de los datos hasta transformar los datos a valores numéricos o a valores categóricos. También en este punto se incluye la estandarización y normalización si se debe hacer.

Podríamos realizar las transformaciones necesarias, como una logarítmica para el atributo *prestador_departamento* (hay mucha diferencia entre Montevideo y los otros departamentos), pero rapidminer, en la mayoría de sus modelos utiliza, o podemos indicarle que utilice, dichas transformaciones.

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-17.png" alt="drawing" width="80%" height="80%"/></div><br/>

#### Dimension reduction

Si las dimensiones son muy grandes, podemos aplicar técnicas que reduzcan la dimensionalidad de los atributos.

Sin embargo este no es el caso, ya que luego de los análisis tenemos dos conjuntos para probar, uno con 11 atributos y otro con 7.

## Modelado
---

En esta sección probamos varios modelos de machine learning. Utilizamos modelos predefinidos en rapdiminer.

Utilizaremos los siguientes modelos:

- ```Logistic Regression``` $\Rightarrow$  [https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/logistic_regression/logistic_regression.html](https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/logistic_regression/logistic_regression.html)
- ```Linear Discriminant Analysis``` $\Rightarrow$ [https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/discriminant_analysis/linear_discriminant_analysis.html](https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/discriminant_analysis/linear_discriminant_analysis.html)
- ```Decision Tree``` $\Rightarrow$ [https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/trees/parallel_decision_tree.html](https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/trees/parallel_decision_tree.html)
- ```Naive Bayes``` $\Rightarrow$ [https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/bayesian/naive_bayes.html](https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/bayesian/naive_bayes.html)
- ```k-NN``` $\Rightarrow$ [https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/lazy/k_nn.html](https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/lazy/k_nn.html)
- ```SVM``` $\Rightarrow$ [https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/support_vector_machines/support_vector_machine.html](https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/support_vector_machines/support_vector_machine.html)
- ```Neural Net``` $\Rightarrow$ [https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/neural_nets/neural_net.html](https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/neural_nets/neural_net.html)
- ```Random Forest``` $\Rightarrow$ [https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/trees/parallel_random_forest.html](https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/trees/parallel_random_forest.html)
- ```Gradient Boosting Trees``` $\Rightarrow$ [https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/trees/gradient_boosted_trees.html](https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/trees/gradient_boosted_trees.html)

Y para chequear la performance de nuestros modelos utilizamos:

- ```Apply Model``` $\Rightarrow$ [https://docs.rapidminer.com/latest/studio/operators/scoring/apply_model.html](https://docs.rapidminer.com/latest/studio/operators/scoring/apply_model.html)
- ```Cross Validation``` $\Rightarrow$ [https://docs.rapidminer.com/latest/studio/operators/validation/cross_validation.html](https://docs.rapidminer.com/latest/studio/operators/validation/cross_validation.html)
- ```Performance``` $\Rightarrow$ [https://docs.rapidminer.com/latest/studio/operators/validation/performance/performance.html](https://docs.rapidminer.com/latest/studio/operators/validation/performance/performance.html)


Utilizaremos ```Optimize Parameters (Evolutionary)``` [https://docs.rapidminer.com/latest/studio/operators/modeling/optimization/parameters/optimize_parameters_evolutionary.html](https://docs.rapidminer.com/latest/studio/operators/modeling/optimization/parameters/optimize_parameters_evolutionary.html) para la optimización del modelo basado en algoritmos evolutivos.

### Preparación del modelado

Los conjuntos a utilizar en el modelado son dos, uno con los atributos correlacionados y otro sin los atributos correlacionados.

### Entrenamiento de los modelos

En esta sección se entrenan los modelos especificados anteriormente para ver cuál es el que realiza la mejor predicción.

#### Logistic Regression

Entrenamiento utilizando regresión logística:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-18.png" alt="drawing" width="80%" height="80%"/></div><br/>

Dentro del proceso de validación cruzada, colocamos el modelo y los operadores para chequear el performance:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-19.png" alt="drawing" width="80%" height="80%"/></div><br/>

Los parámetros utilizados son los estándar de rapidminer.
Una vez entrenamos el modelo, obtenemos los siguientes resultados:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-20.png" alt="drawing" width="80%" height="80%"/></div><br/>

En resumen tenemos una precisión de un **93.42%**.

#### Linear Discriminant Analysis

En este caso, debemos convertir los valores a números utilizando "dummy encoding", ya que es un requerimiento del algoritmo (no maneja valores nominales y rapidminer tampoco los convierte automáticamente). Para esto utilizamos el operador ```Nominal to Numerical``` con la propiedad *dummy coding*

Dentro del proceso de validación cruzada, convertimos los datos a números, colocamos el modelo y los operadores para chequear el performance:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-21.png" alt="drawing" width="80%" height="80%"/></div><br/>

Los parámetros utilizados son los estándar de rapidminer.
Una vez entrenamos el modelo, obtenemos los siguientes resultados:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-22.png" alt="drawing" width="80%" height="80%"/></div><br/>

En resumen tenemos una precisión de un **89.77%**.

En este caso podemos ver que el modelo tiene los siguientes parámetros:

*Linear Discriminant Model*
__Apriori probabilities:__
- AUTORIZADO $\Rightarrow$ 0.8977
- NO AUTORIZADO $\Rightarrow$ 0.1023

El modelo nos da que todos los valores deben ser clasificados como AUTORIZADO, ya que la prioridad Apriori es muy superior que la NO AUTORIZADO. Esto se debe a que la prioridad Apriori es muy alta en comparación con la de NO AUTORIZADO y las probabilidades condicionales no son lo suficientemente grandes para que algún ejemplo se clasifique como NO AUTORIZADO.

#### Decision Tree

Dentro del proceso de validación cruzada, colocamos el modelo y los operadores para chequear el performance:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-23.png" alt="drawing" width="80%" height="80%"/></div><br/>

Los parámetros utilizados son los estándar de rapidminer.
Una vez entrenamos el modelo, obtenemos los siguientes resultados:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-24.png" alt="drawing" width="80%" height="80%"/></div><br/>

En resumen tenemos una precisión de un **92.30%**.

#### Naive Bayes

Dentro del proceso de validación cruzada, colocamos el modelo y los operadores para chequear el performance:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-25.png" alt="drawing" width="80%" height="80%"/></div><br/>

Los parámetros utilizados son los estándar de rapidminer.
Una vez entrenamos el modelo, obtenemos los siguientes resultados:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-26.png" alt="drawing" width="80%" height="80%"/></div><br/>

En resumen tenemos una precisión de un **91.72%**.

#### k-NN

Dentro del proceso de validación cruzada, colocamos el modelo y los operadores para chequear el performance:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-27.png" alt="drawing" width="80%" height="80%"/></div><br/>

Los parámetros utilizados son los estándar de rapidminer.
Una vez entrenamos el modelo, obtenemos los siguientes resultados:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-28.png" alt="drawing" width="80%" height="80%"/></div><br/>

En resumen tenemos una precisión de un **88.08%**.

#### SVM

Dentro del proceso de validación cruzada, convertimos los valores a numéricos, colocamos el modelo y los operadores para chequear el performance:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-29.png" alt="drawing" width="80%" height="80%"/></div><br/>

Los parámetros utilizados son los estándar de rapidminer.
Una vez entrenamos el modelo, obtenemos los siguientes resultados:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-36.png" alt="drawing" width="80%" height="80%"/></div><br/>

En resumen tenemos una precisión de un **93.45%**.

#### Neural Net 

Dentro del proceso de validación cruzada, convertimos los valores a numéricos, colocamos el modelo y los operadores para chequear el performance:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-30.png" alt="drawing" width="80%" height="80%"/></div><br/>

Los parámetros utilizados son los estándar de rapidminer.
Una vez entrenamos el modelo, obtenemos los siguientes resultados:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-37.png" alt="drawing" width="80%" height="80%"/></div><br/>

En resumen tenemos una precisión de un **93.38%**.

#### Random Forest

Dentro del proceso de validación cruzada, colocamos el modelo y los operadores para chequear el performance:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-31.png" alt="drawing" width="80%" height="80%"/></div><br/>

Los parámetros utilizados son los estándar de rapidminer.
Una vez entrenamos el modelo, obtenemos los siguientes resultados:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-38.png" alt="drawing" width="80%" height="80%"/></div><br/>

En resumen tenemos una precisión de un **89.77%**.

#### Gradient Boosting Trees

Dentro del proceso de validación cruzada, colocamos el modelo y los operadores para chequear el performance:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-32.png" alt="drawing" width="80%" height="80%"/></div><br/>

Los parámetros utilizados son los estándar de rapidminer.
Una vez entrenamos el modelo, obtenemos los siguientes resultados:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-39.png" alt="drawing" width="80%" height="80%"/></div><br/>

En resumen tenemos una precisión de un **92.27%**.

### Comparación de modelos

Una vez que tenemos las precisiones de los modelos, podemos comparar las performance de los modelos:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-33.png" alt="drawing" width="80%" height="80%"/></div><br/>

Para el caso de los modelos con los atributos correlaciones filtrados:

| Modelo                 | Performance |
|------------------------|-------------|
| SVM                    | 93.45       |
| Logistic Regression    | 93.42       |
| Neural Net             | 93.38       |
| Decision Tree          | 92.30       |
| Gradient Boosting Tree | 92.27       |
| Naive Bayes            | 91.72       |
| LDA                    | 89.77       |
| Random Forest          | 89.77       |
| k-NN                   | 88.08       |
<br/>

Para el caso de los modelos con los atributos correlaciones no filtrados:

| Modelo                 | Performance |
|------------------------|-------------|
| SVM                    | 92.45       |
| Logistic Regression    | 92.42       |
| Neural Net             | 91.38       |
| Decision Tree          | 91.30       |
| Gradient Boosting Tree | 90.27       |
| LDA                    | 89.77       |
| Naive Bayes            | 89.72       |
| Random Forest          | 85.77       |
| k-NN                   | 81.08       |
<br/>

Podemos ver que el algoritmo que nos brinda la mejor precisión es SVM (Support Vector Machine), y que filtrando los atributos correlacionados nos brinda una mejor predicción.

### Feature selection

Una vez que tenemos el modelo que nos de la mejor perdición, realizamos la selección de atributos utilizando algoritmos evolutivos para observar si se mejora en la predicción o no. En si, esto se debería realizar para cada algoritmo, y luego compararlos, pero consume mucho tiempo este tipo de procesos.

En este caso hay muy pocos atributos, por lo que no es necesaria esta etapa. Sin embargo, probaremos aplicar un algoritmo de reducción de dimensionalidad, aunque no es necesario.

- PCA:
El Análisis de Componentes Principales es una técnica estadística para describir el conjunto de datos en términos de nuevas variables no correlacionados (componentes principales). Los componentes se ordenan por la cantidad de varianza original que describen, por lo que ésta técnica es útil para reducir la dimensionalidad del conjunto.

En rapdiminer el operador utilizado para realizar un Análisis de Componentes Principales es ```Principal Component Analysis``` [https://docs.rapidminer.com/latest/studio/operators/cleansing/dimensionality_reduction/principal_component_analysis.html](https://docs.rapidminer.com/latest/studio/operators/cleansing/dimensionality_reduction/principal_component_analysis.html). 
PCA tiene dos requerimientos importantes:

- Atributos numéricos.
- Estandarización.
- También hay que tener en consideración que el ruido extremo puede afectar al algoritmo.

Lo correcto para utilizar PCA es realizar todas las transformaciones dentro del proceso de validación cruzada:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-40.png" alt="drawing" width="80%" height="80%"/></div><br/>

Si utilizamos un límite de varianza del 95% (esto es perder un 5% de la información), vemos que PCA nos reduce la dimensión en 1. Esto no es mucho, ya que tenemos pocos atributos y no tiene mucho sentido aplicar PCA, pero la reducción de 1 atributo no ha hecho bajar la performance de nuestro modelo, pero si ha bajado la complejidad de los datos lo que ha permitido entrenar más rápido el modelo:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-41.png" alt="drawing" width="80%" height="80%"/></div><br/>

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-42.png" alt="drawing" width="80%" height="80%"/></div><br/>

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-43.png" alt="drawing" width="80%" height="80%"/></div><br/>

Otro dato importante, es que mirando la mantriz de varianza acumulada, podemos ver que la gráfica es casi lineal, lo que implica saltos lineales en la varianza, por lo tanto es un indicio de que hemos seleccionado bien los atributos (todos aportan información al problema):

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-44.png" alt="drawing" width="80%" height="80%"/></div><br/>

### Optimización

En esta sección se optimiza el modelo para utilizarlo en la puesta a producción.

Para optimizar nuestro modelo (elegimos como modelo la Regression Logística, ya que tiene una performance similar a SVM y tiene la ventaja de ser rápido y descriptivo) utilizamos una optimización basada en algoritmos elvolutivos.
Para esto rapidminer nos brinda el operador ```Optimize Parameters (Evolutionary)```:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-45.png" alt="drawing" width="20%" height="20%"/></div><br/>

Dentro de dicho operador colocamos nuestro modelo de validación cruzada:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-46.png" alt="drawing" width="80%" height="80%"/></div><br/>

Luego, en las propiedades del operador de optimización, seleccionamos los parámetros a optimizar. Para el caso de la regresión logística, optimizaremos los siguientes parámetros:

- Lambda (controla la regularización).
- Alhpa (controla las penalidades entre la regularización L1 y L2).
- Stopping tolerance (criterio de parada si no hay mejoras en el modelo).

Una vez ejecutado el modelo, obtenemos el siguiente resultado:

**ParameterSet:**
```
Parameter set:
Performance: 
PerformanceVector [
	-----accuracy: 93.44% +/- 0.18% (micro average: 93.44%)
	
	ConfusionMatrix:
		True:			AUTORIZADO	NO AUTORIZADO
		AUTORIZADO:		21657		1576
		NO AUTORIZADO:	8			894
		-----precision: 99.12% +/- 0.66% (micro average: 99.11%) (positive class: NO AUTORIZADO)

	ConfusionMatrix:
		True:			AUTORIZADO	NO AUTORIZADO
		AUTORIZADO:		21657		1576
		NO AUTORIZADO:	8			894
		-----recall: 36.19% +/- 1.78% (micro average: 36.19%) (positive class: NO AUTORIZADO)

	ConfusionMatrix:
		True:			AUTORIZADO	NO AUTORIZADO
		AUTORIZADO:		21657		1576
		NO AUTORIZADO:	8			894
		-----AUC (optimistic): 0.847 +/- 0.011 (micro average: 0.847) (positive class: NO AUTORIZADO)
		-----AUC: 0.847 +/- 0.011 (micro average: 0.847) (positive class: NO AUTORIZADO)
		-----AUC (pessimistic): 0.847 +/- 0.011 (micro average: 0.847) (positive class: NO AUTORIZADO)
	]
	
Logistic Regression Algorithm (3).lambda	= 1.6837864075475724E308

Logistic Regression Algorithm (3).stopping_tolerance	= 1.74105289675993E308

Logistic Regression Algorithm (3).alpha	= 0.5530535233935917
```

Como podemos ver, ha mejorado muy poco la performance del modelo, pero ha mejorado. 

## Evaluación
---

La evaluación del modelo lo podemos hacer gracias a la potencia de los árboles de decisión y la regresión logística. Éstos permiten explicar porque se toma la decisión adecuada para cada caso.

- Árbol de decisión:
Para el análisis de las decisiones ejecutamos creamos una validación cruzada con un Arbol de decisión como modelo. La diferencia es que en los parámetros del modelos, seteamos que la máxima profundidad del árbol sea 5, ya que esto hace que sea más entendible:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-34.png" alt="drawing" width="80%" height="80%"/></div><br/>

El árbol entrenado, de forma radial, es el siguiente:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-35.png" alt="drawing" width="80%" height="80%"/></div><br/>

Está expresado de forma radial, pero el concepto es el mismo. Fue expresado de esta forma por el motivo de que el atributo que mejor divide a los ejemplos es *prestacion_cod*, y éste atributo tiene muchas categorías, ya que cada prestación es un tipo de enfermedad.
Algunas reglas que podemos obtener del análisis son:

- Para la prestación 801 no se ha autorizado ninguna petición, sin importar el departamento, médico, etc. La prestación 801 corresponde a un trasplante de pulmón. Se supone que la solicitud se realiza ya cuando hay un pulmón "disponible".
- Por otro lado, la prestación 5012, que implica el inicio de un tratamiento de tricoleucemina siempre se ha aprobado.
- Otra prestación que no se ha autorizado nunca es la 2201, que implica al acto medico de RHA (Reproducción Humana Asistida).
- Sin embargo, la prestación 302 tiene un índice de casi 100% de aprobación. Esta prestación corresponde a actos cardíacos, más específicamente a "PCI-ATCP c/cateterismo izq".
- Otro dato importante, es que las prestaciones 1601, 1501, 1602, 1701 y 1503 todas tienen un 100% de aprobación, aunque se producen muy pocos casos en nuestro país. Hubieron exactamente 296 de estas solicitudes. Estas prestaciones incluyen actos médicos a quemados entre otros.
- El atributo *prestacion_cod* permite separar la mayoría de los ejemplos, por lo que vemos que lo importante es la prestación a brindar. Sin embargo, hay algunos casos, como por ejemplo la prestación 5003, que corresponde a tratamientos por Hepatitis C, tiene un porcentaje de autorización del 100% para mujeres, aunque no así para hombres (aunque la proporción es muy pequeña como para sacar alguna conclusión consistente, solo 20 registros se clasificaron así).

## Puesta en producción
---

El pipeline completo se puede ver en la siguiente imagen:

<div style="text-align:center"><img src="{filename}/images/analisis-solicitudes-medicas-47.png" alt="drawing" width="80%" height="80%"/></div><br/>

**Mejoras futuras $\Rightarrow$** Se pueden plantear muchas mejoras futuras, pero algunas recomendadas son las siguientes:

- Realizar el mismo análisis de la evaluación pero incluir los atributos correlacionados, capaz obtenemos alguna diferencia en la evaluación del modelo.
- Intentar obtener más datos de los pacientes.
- En el mismo repositorio se encuentran datos económicos de las prestaciones, una mejora importantes sería incorporar estos datos para saber si la variable económica es un hito importante. Si por ejemplo, la prestación 801 es una de las más caras, podemos obtener un porque tiene un 100% de no autorización.
- Obtener las solicitudes del año 2017 para poder realizar una validación del modelo.
- Utilizar rapidminer server para subir el modelo a la nube y realizar consultas para lograr predicciones.

Podemos obtener el proceso entero en el siguiente link:

- [Rapidminer-Process]({filename}/others/analisis-solicitudes-medicas.rmp)
