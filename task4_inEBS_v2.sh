#Task: Bags in EBS 
#We're using the LMX table. 


#run next line only during first time
#db.lmx.createIndex( {'KEY':1 })

#for testing
##db.lmx.count( { 'KEY': 'INEBS' } )


###


#counting bags 
db.lmx.count({ 'KEY':  'INEBS', 'SUBKEY' : 'TOTAL' , 'CATEGORY': 'BAGSINSYSTEM'})

#list of bags
db.lmx.find({ 'KEY':  'INEBS', 'SUBKEY' : 'TOTAL' , 'CATEGORY': 'BAGSINSYSTEM'})


