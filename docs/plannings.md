# Idea
## Inspiration (Problem)
- Delivery person ko Order deliver krte tym location clearly nahi mil pati, random location names hote hai joki sometimes hard to find hote hai (ex. Near Bustand, but where exactly?). 
- Delivery person has to call the customer (sometimes, more than once) to get to the Delivery Location
- This is Hassle for the customer and Delivery Partner all around the world
- This wastes x amount of time of Deliveries. x amount of Fuel. etc
## Solution
- Building a Standard way to Share Location between Delivery Partners and Customers
- an app jisme Customers apni `location_user_name` bna skte (Like Instagram) or fir Ecommerce Platforms (amazon, flipcart) pe order place krte time dal ske.
- an app Jisme multiple delivery location ko reach krne ke liye Google maps like navigation show hojae for Delivery Partners.  
- an app that can integrate with major Ecommerce Platforms (Amazon, Flipcart, etc).
# Flows
## Customer Flow (1st Approach)
- Before Placing the order on Amazon or Flipkart, customer will make a unique location user name for his house or his property for delivery on our App.
- then, when asked to provide location for placing order, he can type his short and concise `location_user_name` (ex, keshav_house_123) and amazon will parse it as a location_user_name as part of the integration.
## Customer Flow (2nd Approach)
- along with the 1st approach, when placing a order on Amazon or Flipcart, when asked for location, user can create a location username in the Ecommerce client UI. by giving his location with a pin point on a Map UI in the Ecommerce client with the location username. then the Ecommerce Platform sends us the Coordinates and location username and we store that in our database.
- the Ecommerce Platform can implement this by themselves but they might not want to share their location user name with other ecommerce platform, requiring the customer to create location username for each Ecommerce Platform (so tedious). that's why we can help by creating a universally acceptable location username
## Sign up Flow (Customer)
- Inputs
	- log latitude of the House or Property Location 
	- location_user_name for the location
## Sign up Flow (Deliver Person)
- Inputs
	- Delivery Person ki Delivery id with Respective to the Platform
	- Person Details
		- Name
## Order place flow
- Build a Simple form to fill out order details mention in integration Dependencies
## Delivery Person Flow
- Hame Delivery person ko Ecommerce Platform ke Db se order location ke best path ko show krna hai.
- Amazon, flipkart pe order place ho tab, unke order ke sath hmari location id bhi store ho jae. or delivery person us location id ko hmare frontend me use kr ske or Google Maps like Navigation usko show hojae.
- Deliver Person ke frontend pe Best Route show krna hai. ( either using google maps apis or mannualy )
# Integration Dependencies
- Inputs
	- Order Related
		- Order ID
		- Location Id
		- Order Name
	- Delivery Related
		- delivery Person ki id
## Privacy Concerns
- making any location user name accessible to the delivery partner can pose a ethical risk. 
- he can randomly type a location user name. and know a real person's house address. which he might use for Unethical activities

## Presentation Planning
- Flow Diagram
- Protype of the product
- Video Template
- Reference Video


- [ ] Sign up Flow (Customer)
	- [ ] User can input location with log latitude or Pin 
	- [ ] we will map this data to a unique user_name like ID (Like Instagram)
- [ ] Sign up Flow (Deliver Person)
	- [ ] Delivery Person ki Delivery id with Respective to the Platform
	- [ ] Person Details
		- [ ] Name
- [ ] Order place flow
	- [ ] Build a Simple form to fill out order details mention in integration Dependencies
- [ ] Delivery Person Flow
	- [ ] Hame Delivery person ko Amazon ke Db se order location ke best path ko show krna hai.
	- [ ] Amazon, flipkart pe order place ho tab, unke order ke sath hmari location id bhi store ho jae. or delivery person us location id ko hmare frontend me use kr ske or Google Maps like Navigation usko show hojae.
	- [ ] Deliver Person ke frontend pe Best Route show krna hai. ( either using google maps apis or mannualy )
# Ai Feature (Phase 2)
- [ ] Customer Ke liye Chatbot jo ki
	- [ ] Customer ke Order ki Information compile kr ke de ske
# Entity States
- [ ] Order States
	- [ ] Pending
	- [ ] Resolved
- [ ] User States
	- [ ] Delivery Person
	- [ ] Customer
	- [ ] Admin

## Premature Planning
- [ ] Create a Presentation Video for Google Maps Hackathon Challenge
- [ ] Steps we can Follow
	- [x] Define the Exact Idea that's regarding the Delivery Guy Helper Idea
	- [ ] Define an Architecture
	- [ ] Choose The Tech Stack that's everyone is most comfortable in
	- [ ] Decide what need to Done first Quickly for sending a Demo Presentation Video to GOogle
	- [ ] Distribute the Tasks
