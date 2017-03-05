
#Read the csv file of the service mapping
lines = open ('service-mappings.txt', 'r').read().splitlines()

#empty the array
array = []
counter = 1

for line in lines:
    #clean the input
    line = line.rstrip()
    #split the line
    line_list = line.split(',')
    #count the service-component
    number_of_service_component = len(line_list)
    #create the service mapping soap
    print '<service-map index="%d">' %counter

    for item in line_list[:-1]:
        print '<service-component>\n\
               <qualified-name>Cosmote Greece/%s</qualified-name>\n\
               </service-component>' %item
    print '<pep-profile><qualified-name>%s</qualified-name></pep-profile>\n' % line_list[-1]
    counter =counter+1
