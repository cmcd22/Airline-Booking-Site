An assignment for my third-year course for Advanced Web Development.

Using a Django framework, a site for a fictional airline was created. Users can book flights, check flight schedules and cancel bookings.

When loading this app for the first time, it's important that you navigate
to the /home page first, which allows the database to be populated with flight
information (this may take a few seconds). All subsequent visits should also visit this page first in order
for table information to be updated accordingly.
Bookings will be maintained between sessions unless the flight date has
already passed, in which case, the booking will be removed from the system.
Once a flight's departure time has passed, it will be hidden from database
queries and searches. Once its date has passed, the flight will be deleted
from the system.
The database contains 3 tables; a Customer/User table, a Flights table and a
Booking table which acts as a Junction between the two.
The app doesn't feature a login system, but a customer's bookings can be
accessed by entering their email address in the Cancel Booking section.
