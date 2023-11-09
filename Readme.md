BIM Execution Plan

Introduction:
We have chosen to work with the structural use case where we focus on the calculation of structural elements. We find the total length of the beams in the project and estimate a total price based on profile type. The use case is for customers that want an estimated price of the structural elements in their project.

GOALS

Scope:
The project focuses on beams as structural elements and excludes other types of structual elements such as columns and walls. The goals are to assign a price property to different structural elements to make it easier to estimate a total price.

MODEL USES

Roles and responsibilities:
Architects are responsible for creating the model.
Engineers are responsible for calculating dimensions of structural elements and verification of model, and estimating the total price.
Construction workers are responsible for building the desired construction based on the materials from the architect and the engineer.

PROCESS

According to the current BPMN-diagram, a custumer wants a structural element in a project and contacts an architect for a model. The architect create a model for the project and stores it as an IFC-file and hands it over to the engineer. The engineer selects data for the desired structural elements, and adds price properties, and extract these datas. Based on this, the engineer calculates dimensions and costs of the structural elements and hands it over to the custumer. There is communication between the costumer and the engineer, where they agree on the solution, with and iterative process if the costumer wants changes. The custumer hands over the received informations to the contruction worker which finished the process.  

<img src="BPMN_current.svg ">

Tool/workflow:
We will focus on adding a property of price to the structural elements in the project, which will make it possible to make a more exact price estimation.

IFC:
We're focusing on the lenght of beams as a property in the IFC-file, and an addtional property for price, which is added to the IFC-file. 

Development of program:
Firstly, we find and select all beams in the model. Afterwards, we find and select the length property of beams and use the length for calculation the total length of the beams in project. Lastly, we add a price property to each profile type, to estimate a total cost of the beams as strucutral elements. 

BIM implementation costs:
The engineer utilizies the program to estimate a cost for beams as structural elements based on the total length of beams in the project. The price for the beams differs for each profile type (HEB, IPE and ect.).

Risk management:
An error in the model due to lack of material properties assigned to strucural elements such as length. Another error could be calling the wrong property of the structural element entaling using a wrong parameter and getting a wrong result of cost estimation.  

BIM execution plan review and approval:
Agreement between all parts regarding the excution plan of the project. 

INFORMATION EXCHANGE

When the IFC-model is recieved, the LOD is 300 because there's inforation of the elements as size and quantity and the geometry is correct but no further information. After we have added properties to elements, the model becomes a LOD 400 due to more detailed informtions regarding fabrication.    

WHAT POTENTIAL IMPROVEMENTS OFFER

Describe the business value:
Better cooperation between different parts (engineer, architect and intrapreneur), as all material and calculations are included in a single file (IFC). Which entails less wasted time, and more efficient workflow. 

Additional BPMN file:
<img src="BPMN_additions.svg ">

Describe the societal value:
Due to the optimized dimensions for structural elements, there will be less material waste, which entails less CO2 emissions.




