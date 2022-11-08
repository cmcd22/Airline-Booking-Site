from django.shortcuts import render
from django.http import HttpResponse
from datetime import *
from datetime import datetime
from myapp.models import Flights,Customer,Bookings
import random

def home(request):
    dbCheck = Flights.objects.all().order_by('departureDate')
    today = date.today()
    if not dbCheck:
        finalDate = today.replace(year = today.year + 1)
        currentDate = today
        newDateFormat = currentDate.strftime("%Y-%m-%d")
        day = timedelta(days=1)
        iterator = datetime.now().timetuple().tm_yday

        while currentDate < finalDate:
            # Monday
            if currentDate.weekday() == 0:
                flights = [
                    ('DFR'+str(iterator)+'1','Dairy Flat','Rotorua','00:45','08:00','08:45',currentDate,'$150',4,newDateFormat),
                    ('RDF'+str(iterator)+'1','Rotorua','Dairy Flat','00:45','12:00','12:45',currentDate,'$150',4,newDateFormat),
                    ('DFR'+str(iterator)+'2','Dairy Flat','Rotorua','00:45','16:00','16:45',currentDate,'$150',4,newDateFormat),
                    ('RDF'+str(iterator)+'2','Rotorua','Dairy Flat','00:45','20:00','20:45',currentDate,'$150',4,newDateFormat),
                    ('DFGB'+str(iterator),'Dairy Flat','Great Barrier Island','00:30','09:00','09:30',currentDate,'$150',4,newDateFormat),
                    ('DFLT'+str(iterator),'Dairy Flat','Lake Tekapo','01:45','10:00','11:45',currentDate,'$250',5,newDateFormat)
                ]
            # Tuesday
            elif currentDate.weekday() == 1:
                flights = [
                    ('DFR'+str(iterator)+'1','Dairy Flat','Rotorua','00:45','08:00','08:45',currentDate,'$150',4,newDateFormat),
                    ('RDF'+str(iterator)+'1','Rotorua','Dairy Flat','00:45','12:00','12:45',currentDate,'$150',4,newDateFormat),
                    ('DFR'+str(iterator)+'2','Dairy Flat','Rotorua','00:45','16:00','16:45',currentDate,'$150',4,newDateFormat),
                    ('RDF'+str(iterator)+'2','Rotorua','Dairy Flat','00:45','20:00','20:45',currentDate,'$150',4,newDateFormat),
                    ('GBDF'+str(iterator),'Great Barrier Island','Dairy Flat','00:30','08:00','08:30',currentDate,'$150',4,newDateFormat),
                    ('DFCI'+str(iterator),'Dairy Flat','Chatham Islands','02:15','12:00','15:00',currentDate,'$500',5,newDateFormat)
                ]
            # Wednesday
            elif currentDate.weekday() == 2:
                flights = [
                    ('DFR'+str(iterator)+'1','Dairy Flat','Rotorua','00:45','08:00','08:45',currentDate,'$150',4,newDateFormat),
                    ('RDF'+str(iterator)+'1','Rotorua','Dairy Flat','00:45','12:00','12:45',currentDate,'$150',4,newDateFormat),
                    ('DFR'+str(iterator)+'2','Dairy Flat','Rotorua','00:45','16:00','16:45',currentDate,'$150',4,newDateFormat),
                    ('RDF'+str(iterator)+'2','Rotorua','Dairy Flat','00:45','20:00','20:45',currentDate,'$150',4,newDateFormat),
                    ('DFGB'+str(iterator),'Dairy Flat','Great Barrier Island','00:30','09:00','09:30',currentDate,'$150',4,newDateFormat),
                    ('CIDF'+str(iterator),'Chatham Islands','Dairy Flat','02:45','12:00','14:00',currentDate,'$500',5,newDateFormat)
                ]
            # Thursday
            elif currentDate.weekday() == 3:
                flights = [
                    ('DFR'+str(iterator)+'1','Dairy Flat','Rotorua','00:45','08:00','08:45',currentDate,'$150',4,newDateFormat),
                    ('RDF'+str(iterator)+'1','Rotorua','Dairy Flat','00:45','12:00','12:45',currentDate,'$150',4,newDateFormat),
                    ('DFR'+str(iterator)+'2','Dairy Flat','Rotorua','00:45','16:00','16:45',currentDate,'$150',4,newDateFormat),
                    ('RDF'+str(iterator)+'2','Rotorua','Dairy Flat','00:45','20:00','20:45',currentDate,'$150',4,newDateFormat),
                ]
            # Friday
            elif currentDate.weekday() == 4:
                flights = [
                    ('DFR'+str(iterator)+'1','Dairy Flat','Rotorua','00:45','08:00','08:45',currentDate,'$150',4,newDateFormat),
                    ('RDF'+str(iterator)+'1','Rotorua','Dairy Flat','00:45','12:00','12:45',currentDate,'$150',4,newDateFormat),
                    ('DFR'+str(iterator)+'2','Dairy Flat','Rotorua','00:45','16:00','16:45',currentDate,'$150',4,newDateFormat),
                    ('RDF'+str(iterator)+'2','Rotorua','Dairy Flat','00:45','20:00','20:45',currentDate,'$150',4,newDateFormat),
                    ('DFS'+str(iterator),'Dairy Flat','Sydney','04:30','14:00','16:30',currentDate,'$5000',6,newDateFormat),
                    ('RS'+str(iterator),'Rotorua','Sydney','03:30','15:00','16:30',currentDate,'$4800',6,newDateFormat),
                    ('DFGB'+str(iterator),'Dairy Flat','Great Barrier Island','00:30','09:00','09:30',currentDate,'$150',4,newDateFormat),
                    ('GBDF'+str(iterator),'Great Barrier Island','Dairy Flat','00:30','08:00','08:30',currentDate,'$150',4,newDateFormat),
                    ('DFCI'+str(iterator),'Dairy Flat','Chatham Islands','02:15','12:00','15:00',currentDate,'$500',5,newDateFormat),
                    ('LTDF'+str(iterator),'Lake Tekapo','Dairy Flat','01:45','10:00','11:45',currentDate,'$250',5,newDateFormat)
                ]
            # Saturday
            elif currentDate.weekday() == 5:
                flights = [
                    ('GBDF'+str(iterator),'Great Barrier Island','Dairy Flat','00:30','08:00','08:30',currentDate,'$150',4,newDateFormat),
                    ('CIDF'+str(iterator),'Chatham Islands','Dairy Flat','02:45','12:00','14:00',currentDate,'$500',5,newDateFormat)
                ]
            # Sunday
            else:
                flights = [
                    ('SDF'+str(iterator),'Sydney','Dairy Flat','03:15','15:00','20:15',currentDate,'$5000',6,newDateFormat)
                ]

            for flightNo,origin,destination,duration,departureTime,arrivalTime,departureDate,price,totalSeats,newDateFormat in flights:
                f = Flights(flightNo,origin,destination,duration,departureTime,arrivalTime,departureDate,price,totalSeats,newDateFormat)
                f.save()
            currentDate = currentDate + day
            newDateFormat = currentDate.strftime("%Y-%m-%d")
            if iterator >= 365:
                iterator = 1
            else:
                iterator += 1
    else:
        firstDate = dbCheck[0].departureDate
        if firstDate != today:
            bookingsCheck = Bookings.objects.all()
            if bookingsCheck:
                for x in bookingsCheck:
                    if x.flight.departureDate < today:
                        x.delete()
            for y in dbCheck:
                if y.departureDate < today:
                    y.delete()
    return render(request, 'home.html', {})

def flights(request):
    today = date.today()
    t = datetime.now()
    time = t.strftime('%H:%M:%S:')
    hours = time.split(':')[0]
    minutes = time.split(':')[1]
    allFlights = Flights.objects.exclude(departureTime='Gone').order_by('departureDate')
    excludedFlights = []
    for x in allFlights:
        if x.departureDate == today:
            depHour = x.departureTime.split(':')[0]
            depMinute = x.departureTime.split(':')[1]
            if hours > depHour:
                excludedFlights.append(x.flightNo)
            elif hours == depHour and minutes > depMinute:
                excludedFlights.append(x.flightNo)
    for num in excludedFlights:
        f = Flights.objects.get(flightNo=num)
        f.departureTime = 'Gone'
        f.save()
    allFlights = Flights.objects.exclude(departureTime='Gone').order_by('departureDate')
    context = {'allFlights': allFlights}
    return render(request, 'flights.html', context)

def cancel(request):
    allBookings = Bookings.objects.all()
    context = {'allBookings': allBookings}
    return render(request, 'cancel.html', context)

def getBooking(request):
    if request.method == 'POST':
        email = request.POST['email']
        bookings = Bookings.objects.all().filter(cust=email)
        if not bookings:
            text = '<h3><u>*No bookings found under this address*</u></h3>'
        else:
            text1 = """<tr><td><b>Booking Number</b></td>
                    <td><b>Date</b></td>
                    <td><b>Flight Number</b></td>
                    <td><b>Origin</b></td>
                    <td><b>Destination</b></td>
                    <td><b>Price</b></td></tr>"""
            text2 = ''
            for x in bookings:
                text2 += '<tr class="selectableRows"><td>'+str(x.bRef)+'</td><td>'+str(x.flight.departureDate)+'</td><td>'+x.flight.flightNo+'</td><td>'+x.flight.origin+'</td><td>'+x.flight.destination+'</td><td>'+x.flight.price+'</td><td><button onclick="selectBooking(this)">Cancel</td></tr>'
            text = text1 + text2
        return HttpResponse(text)
    else:
        bNumber = request.GET['bNumber']
        try:
            booking = Bookings.objects.get(bRef=bNumber)
        except:
            text = '<h3><u>*Booking number not found*</u></h3>'
        else:
            text = '<h4><u>Name:</u> <span>'+booking.cust.firstName+' '+booking.cust.lastName+'</span></h4><h4><u>Flight Number:</u> <span>'+booking.flight.flightNo+'</span></h4><h4><u>Departure Date:</u> <span>'+str(booking.flight.departureDate)+'</span></h4><h4><u>Leaving From:</u> <span>'+booking.flight.origin+'</span></h4><h4><u>Going To:</u> <span>'+booking.flight.destination+'</span></h4>'
        return HttpResponse(text)



def deleteBooking(request):
    bNumber = request.POST['bNumber']
    booking = Bookings.objects.get(bRef=bNumber)
    booking.delete()
    text = '<h4> Booking has been successfully cancelled</h4>'
    return HttpResponse(text)

def confirmationoneway(request):
    if request.method == 'POST':
        flightNo = request.POST['flightNo']
        allFlights = Flights.objects.exclude(departureTime='Gone')
        correctFlight = allFlights.filter(flightNo=flightNo)
        bookingR = 0;
        while True:
            bookingR = random.randint(10000000, 99999999)
            allBookings = Bookings.objects.all()
            matching = allBookings.filter(bRef=bookingR)
            if not matching:
                break;
        allCustomers = Customer.objects.all()
        existingCustomer = allCustomers.filter(email=request.POST['email'])
        if not existingCustomer:
            c = Customer(
            email = request.POST['email'],
            firstName = request.POST['firstName'],
            lastName = request.POST['lastName'],
            phone = request.POST['phone'],
            ppNumber = request.POST['passport']
            )
            c.save()
        b = Bookings(
        bRef = bookingR,
        cust = Customer.objects.get(email=request.POST['email']),
        flight = Flights.objects.get(flightNo=flightNo),
        time = datetime.now()
        )
        b.save()
        text = 'ok'
        return HttpResponse(text)
    else:
        info = Bookings.objects.last()
        context = {'info': info}
        return render(request, 'confirmationoneway.html',context)

def confirmationreturn(request):
    if request.method == 'POST':
        flightNo1 = request.POST['flightNo1']
        flightNo2 = request.POST['flightNo2']
        allFlights = Flights.objects.exclude(departureTime='Gone')
        correctFlight1 = allFlights.filter(flightNo=flightNo1)
        correctFlight2 = allFlights.filter(flightNo=flightNo2)
        bookingR1 = 0;
        bookingR2 = 0;
        while True:
            bookingR1 = random.randint(10000000, 99999999)
            bookingR2 = random.randint(10000000, 99999999)
            if bookingR1 == bookingR2:
                continue
            allBookings = Bookings.objects.all()
            matching1 = allBookings.filter(bRef=bookingR1)
            matching2 = allBookings.filter(bRef=bookingR2)
            if not matching1 and not matching2:
                break;
        allCustomers = Customer.objects.all()
        existingCustomer = allCustomers.filter(email=request.POST['email'])
        if not existingCustomer:
            c = Customer(
            email = request.POST['email'],
            firstName = request.POST['firstName'],
            lastName = request.POST['lastName'],
            phone = request.POST['phone'],
            ppNumber = request.POST['passport']
            )
            c.save()
        b1 = Bookings(
        bRef = bookingR1,
        cust = Customer.objects.get(email=request.POST['email']),
        flight = Flights.objects.get(flightNo=flightNo1),
        time = datetime.now()
        )
        b1.save()
        b2 = Bookings(
        bRef = bookingR2,
        cust = Customer.objects.get(email=request.POST['email']),
        flight = Flights.objects.get(flightNo=flightNo2),
        time = datetime.now()
        )
        b2.save()
        text = 'ok'
        return HttpResponse(text)
    else:
        all = Bookings.objects.all().order_by("-time")
        both = all[:2]
        context = {'info': both}
        return render(request, 'confirmationreturn.html',context)

def book(request):
    today = date.today()
    t = datetime.now()
    time = t.strftime('%H:%M:%S:')
    hours = time.split(':')[0]
    minutes = time.split(':')[1]
    allFlights = Flights.objects.exclude(departureTime='Gone').order_by('departureDate')
    excludedFlights = []
    for x in allFlights:
        if x.departureDate == today:
            depHour = x.departureTime.split(':')[0]
            depMinute = x.departureTime.split(':')[1]
            if hours > depHour:
                excludedFlights.append(x.flightNo)
            elif hours == depHour and minutes > depMinute:
                excludedFlights.append(x.flightNo)
    for num in excludedFlights:
        f = Flights.objects.get(flightNo=num)
        f.departureTime = 'Gone'
        f.save()
    allFlights = Flights.objects.exclude(departureTime='Gone').order_by('departureDate')
    context = {'allFlights': allFlights}
    return render(request, 'book.html', context)

def bookoneway(request,flight):
    if request.method == 'POST':
        text = 'ok'
        return HttpResponse(text)
    else:
        flight = Flights.objects.get(flightNo=flight)
        context = {'flight': flight}
        return render(request, 'bookoneway.html',context)


def getflightsOW(request):
    date = request.POST['date']
    orig = request.POST['origin']
    dest = request.POST['destination']
    allFlights = Flights.objects.exclude(departureTime='Gone')
    correctDate = allFlights.filter(newDateFormat=date)
    correctOrigin = correctDate.filter(origin=orig)
    correctDest = correctOrigin.filter(destination=dest)
    if not correctDest:
        text = '<h4>No flights match the given criteria (NOTE: '
        if orig == 'Chatham Islands':
            ammend = 'This service is only available Wednesdays and Saturdays'
        elif orig == 'Dairy Flat':
            if dest == 'Chatham Islands':
                ammend = 'This service is only available Tuesdays and Fridays'
            elif dest == 'Great Barrier Island':
                ammend = 'This service is only available Mondays, Wednesdays and Fridays'
            elif dest == 'Lake Tekapo':
                ammend = 'This service is only available on Mondays'
            elif dest == 'Rotorua':
                ammend = 'This service is only available from Monday to Friday'
            elif dest == 'Sydney':
                ammend = 'This service is only available on Fridays'
        elif orig == 'Great Barrier Island':
            ammend = 'This service is only available Tuesdays, Fridays and Saturdays'
        elif orig == 'Lake Tekapo':
            ammend = 'This service is only available on Fridays'
        elif orig == 'Rotorua':
            if dest == 'Dairy Flat':
                ammend = 'This service is only available from Monday to Friday'
            else:
                ammend = 'This service is only available on Fridays'
        else:
            ammend = 'This service is only available on Sundays'
        finalText = text + ammend
        finalText += ')</h4>'
        return HttpResponse(finalText)
    else:
        warning = False
        text = """<tr><th><b>Date</b></th>
                <th><b>Flight Number</b></th>
                <th><b>Leaving From</b></th>
                <th><b>Going To</b></th>
                <th><b>Duration</b></th>
                <th><b>Departure Time</b></th>
                <th><b>Arrival Time</b></th>
                <th><b>Price</b></th>
                <th><b>Seats</b></th></tr>"""
        text2 = ''
        for x in correctDest:
            fn = x.flightNo
            numbers = Bookings.objects.filter(flight=fn)
            n = len(numbers)
            seats = x.totalSeats-n
            if dest == 'Sydney':
                splitFlight = fn.split('S')[1]
                if orig == 'Dairy Flat':
                    otherFlight = 'RS'+splitFlight
                else:
                    otherFlight = 'DFS'+splitFlight
                otherF = Bookings.objects.filter(flight=otherFlight)
                otherSeats = len(otherF)
                seats -= otherSeats
            if seats == 0:
                warning = True
                continue
            text2 += '<tr class="selectableRows"><td>'+str(x.departureDate)+'</td><td>'+x.flightNo+'</td><td>'+x.origin+'</td><td>'+x.destination+'</td><td>'+x.duration+'</td><td>'+x.departureTime+'</td><td>'+x.arrivalTime+'</td><td>'+x.price+'</td><td>'+str(seats)+'</td><td><button onclick="finalSelection(this)">Select</td></tr>'

        if warning and text2 == '':
            text = '<h4>All flights on this day have sold out</h4>'
            finalText = text
        elif warning:
            text2 += '<h4>NOTE: Some flights on this date are not displayed as they have sold out</h4>'
            finalText = text + text2
        else:
            finalText = text + text2

        return HttpResponse(finalText)

def getflightsR(request):
    depDate = request.POST['depDate']
    retDate = request.POST['retDate']
    orig = request.POST['origin']
    dest = request.POST['destination']
    allFlights = Flights.objects.exclude(departureTime='Gone')
    correctDate1 = allFlights.filter(newDateFormat=depDate)
    correctOrigin1 = correctDate1.filter(origin=orig)
    correctDest1 = correctOrigin1.filter(destination=dest)
    returnOrig = dest
    returnDest = orig
    if orig == 'Rotorua' and dest == 'Sydney':
        returnDest = 'Dairy Flat'
    correctDate2 = allFlights.filter(newDateFormat=retDate)
    correctOrigin2 = correctDate2.filter(origin=returnOrig)
    correctDest2 = correctOrigin2.filter(destination = returnDest)
    if not correctDest1:
        text1 = '<h4>No outbound flights match the given criteria (NOTE: '
        if orig == 'Chatham Islands':
            ammend1 = 'This service is only available Wednesdays and Saturdays'
        elif orig == 'Dairy Flat':
            if dest == 'Chatham Islands':
                ammend1 = 'This service is only available Tuesdays and Fridays'
            elif dest == 'Great Barrier Island':
                ammend1 = 'This service is only available Mondays, Wednesdays and Fridays'
            elif dest == 'Lake Tekapo':
                ammend1 = 'This service is only available on Mondays'
            elif dest == 'Rotorua':
                ammend1 = 'This service is only available from Monday to Friday'
            elif dest == 'Sydney':
                ammend1 = 'This service is only available on Fridays'
        elif orig == 'Great Barrier Island':
            ammend1 = 'This service is only available Tuesdays, Fridays and Saturdays'
        elif orig == 'Lake Tekapo':
            ammend1 = 'This service is only available on Fridays'
        elif orig == 'Rotorua':
            if dest == 'Dairy Flat':
                ammend1 = 'This service is only available from Monday to Friday'
            else:
                ammend1 = 'This service is only available on Fridays'
        else:
            ammend1 = 'This service is only available on Sundays'
        combText1 = text1 + ammend1
        text1 = combText1 + ')</h4>'
        finalText1 = text1
    else :
        warning1 = False
        text1 = 'Outgoing Flights:<br>'
        text1 += """<tr><td><b>Date</b></td>
                <td><b>Flight Number</b></td>
                <td><b>Leaving From</b></td>
                <td><b>Going To</b></td>
                <td><b>Duration</b></td>
                <td><b>Departure Time</b></td>
                <td><b>Arrival Time</b></td>
                <td><b>Price</b></td>
                <td><b>Seats</b></td></tr>"""
        text2 = ''
        for x in correctDest1:
            fn1 = x.flightNo
            numbers1 = Bookings.objects.filter(flight=fn1)
            n1 = len(numbers1)
            seats1 = x.totalSeats-n1
            if dest == 'Sydney':
                splitFlight = fn1.split('S')[1]
                if orig == 'Dairy Flat':
                    otherFlight = 'RS'+splitFlight
                else:
                    otherFlight = 'DFS'+splitFlight
                otherF = Bookings.objects.filter(flight=otherFlight)
                otherSeats = len(otherF)
                seats1 -= otherSeats
            if seats1 == 0:
                warning1 = True
                continue
            text2 += '<tr><td>'+str(x.departureDate)+'</td><td>'+x.flightNo+'</td><td>'+x.origin+'</td><td>'+x.destination+'</td><td>'+x.duration+'</td><td>'+x.departureTime+'</td><td>'+x.arrivalTime+'</td><td>'+x.price+'</td><td>'+str(seats1)+'</td><td><button onclick="finalSelectionRet1(this)">Select</td></tr>'
        if warning1 and text2 == '':
            text2 = '<h4>All flights on this day have sold out</h4>'
            finalText1 = text2
        elif warning1:
            text2 += '<h4>NOTE: Some flights on this date are not displayed as they have sold out</h4>'
            finalText1 = text1 + text2
        else:
            finalText1 = text1 + text2
    if not correctDest2:
        text3 = '<h4>No return flights match the given criteria (NOTE: '
        if returnOrig == 'Chatham Islands':
            ammend2 = 'This service is only available Wednesdays and Saturdays'
        elif returnOrig == 'Dairy Flat':
            if returnDest == 'Chatham Islands':
                ammend2 = 'This service is only available Tuesdays and Fridays'
            elif returnDest == 'Great Barrier Island':
                ammend2 = 'This service is only available Mondays, Wednesdays and Fridays'
            elif returnDest == 'Lake Tekapo':
                ammend2 = 'This service is only available on Mondays'
            elif returnDest == 'Rotorua':
                ammend2 = 'This service is only available from Monday to Friday'
            elif returnDest == 'Sydney':
                ammend2 = 'This service is only available on Fridays'
        elif returnOrig == 'Great Barrier Island':
            ammend2 = 'This service is only available Tuesdays, Fridays and Saturdays'
        elif returnOrig == 'Lake Tekapo':
            ammend2 = 'This service is only available on Fridays'
        elif returnOrig == 'Rotorua':
            if returnDest == 'Dairy Flat':
                ammend2 = 'This service is only available from Monday to Friday'
            else:
                ammend2 = 'This service is only available on Fridays'
        else:
            ammend2 = 'This service is only available on Sundays'
        combText2 = text3 + ammend2
        text3 = combText2 + ')</h4>'
        finalText2 = text3
    else :
        warning2 = False
        text3 = 'Return Flights:<br>'
        text3 += """<tr><td><b>Date</b></td>
                <td><b>Flight Number</b></td>
                <td><b>Leaving From</b></td>
                <td><b>Going To</b></td>
                <td><b>Duration</b></td>
                <td><b>Departure Time</b></td>
                <td><b>Arrival Time</b></td>
                <td><b>Price</b></td>
                <td><b>Seats</b></td></tr>"""
        text4 = ''
        for y in correctDest2:
            fn2 = y.flightNo
            numbers2 = Bookings.objects.filter(flight=fn2)
            n2 = len(numbers2)
            seats2 = y.totalSeats-n2
            if seats2 == 0:
                warning2 = True
                continue
            text4 += '<tr><td>'+str(y.departureDate)+'</td><td>'+y.flightNo+'</td><td>'+y.origin+'</td><td>'+y.destination+'</td><td>'+y.duration+'</td><td>'+y.departureTime+'</td><td>'+y.arrivalTime+'</td><td>'+y.price+'</td><td>'+str(seats2)+'</td><td><button onclick="finalSelectionRet2(this)">Select</td></tr>'
        if warning2 and text4 == '':
            text4 = '<h4>All flights on this day have sold out</h4>'
            finalText2 = text4
        elif warning2:
            text4 += '<h4>NOTE: Some flights on this date are not displayed as they have sold out</h4>'
            finalText2 = text3 + text4
        else:
            finalText2 = text3 + text4
    finalText = finalText1 +'#' + finalText2
    return HttpResponse(finalText)
