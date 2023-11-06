import datetime
from datetime import datetime
from flask import Blueprint, jsonify, request, render_template, redirect, session, url_for, flash
from app.models.Bookings import Booking
from app.views.decorators import user_logged_in
from ..models import Room, Token
from ..config.database import db

room = Blueprint("room", __name__) 

# To add a new room
@room.route("/room", methods=["POST"])
def room_page():
    if request.method == "POST":
        # Get data from the form.
        name = request.form.get("room_name")
        image1 = request.form.get("image1")
        image2 = request.form.get("image2")
        image3 = request.form.get("image3")
        description = request.form.get("description")
        max_occupancy = request.form.get("max_occupancy")
        view = request.form.get("view")
        status = request.form.get("status")
        price = request.form.get("price")
        width = request.form.get("width")

        print(f"request : {request.form}")

        # Check if required fields are not empty.
        if not image1 or not description or not max_occupancy or not price:
            flash("Please provide values for required fields", "error")
            return redirect(url_for("admin.room_page"))

        # Validate max_occupancy is a positive integer.
        if not max_occupancy.isnumeric() or int(max_occupancy) <= 0:
            flash("Max occupancy must be a positive integer", "error")
            return redirect(url_for("admin.room_page"))

        # Validate price is a positive float.
        try:
            price = float(price)
            if price <= 0:
                raise ValueError
        except ValueError:
            flash("Price must be a positive number", "error")
            return redirect(url_for("admin.room_page"))

        # Create a Room instance and add it to the database.
        new_room = Room(room_name=name, image1=image1, image2=image2, image3=image3, view=view, width=width,
                        max_occupancy=int(max_occupancy), price=price, description=description, status=status)
        db.session.add(new_room)
        db.session.commit()

        # Redirect to the page where you want to show the updated list of rooms.
        flash("Room added successfully", "success")
        return redirect(url_for("admin.room_page"))

# To update existing room
@room.route("/room/update/<int:room_id>", methods=["POST"])
def update_room(room_id):
 if request.method == "POST":
    # Get data from the form.
    room_name = request.form.get("room_name")
    description = request.form.get("description")
    max_occupancy = request.form.get("max_occupancy")
    view = request.form.get("view")
    status = request.form.get("status")
    price = request.form.get("price")
    width = request.form.get("width")

    # Check if required fields are not empty.
    if not room_name or not description or not max_occupancy or not price:
        flash("Please provide values for required fields", "error")
        return redirect(url_for("admin.room_page"))

    # Validate max_occupancy is a positive integer.
    if not max_occupancy.isnumeric() or int(max_occupancy) <= 0:
        flash("Max occupancy must be a positive integer", "error")
        return redirect(url_for("admin.room_page"))

    # Validate price is a positive float.
    try:
        price = float(price)
        if price <= 0:
            raise ValueError
    except ValueError:
        flash("Price must be a positive number", "error")
        return redirect(url_for("admin.room_page"))

    # Retrieve the original image values from the database.
    room = Room.query.get(room_id)
    if room:
        original_image1 = room.image1
        original_image2 = room.image2
        original_image3 = room.image3

        # Update room details in the database.
        room.room_name = room_name
        room.image1 = original_image1
        room.image2 = original_image2
        room.image3 = original_image3
        room.view = view
        room.width = width
        room.max_occupancy = int(max_occupancy)
        room.price = price
        room.description = description
        room.status = status

        db.session.commit()

        flash("Room details updated successfully", "success")
    else:
        flash("Room not found", "error")

    # Redirect back to the room details page.
    return redirect(url_for("admin.room_page"))

@room.route("/update_images/<int:room_id>", methods=['POST'])
def update_images(room_id):
    if request.method == "POST":
        # Get new image URLs from the form.
        new_image1 = request.form.get("image1")
        new_image2 = request.form.get("image2")
        new_image3 = request.form.get("image3")

        # Retrieve the room from the database.
        room = Room.query.get(room_id)
        if room:
            # Update the image URLs in the room object.
            room.image1 = new_image1
            room.image2 = new_image2
            room.image3 = new_image3

            # Commit the changes to the database.
            db.session.commit()

            flash("Room images updated successfully", "success")
        else:
            flash("Room not found", "error")

    # Redirect back to the room details page.
    return redirect(url_for("admin.room_page"))

# TO book a particular room
@room.route("/book-room/<int:room_id>", methods=["GET", "POST"])
@user_logged_in
def book_room(room_id):
    if request.method == "POST":
        # Get form data
        date_of_arrival_str = request.form.get("date_of_arrival")
        date_of_departure_str = request.form.get("date_of_departure")

        date_of_arrival = datetime.strptime(date_of_arrival_str, '%Y-%m-%d').date()
        date_of_departure = datetime.strptime(date_of_departure_str, '%Y-%m-%d').date()
        # Check if the arrival date is before the departure date
        if date_of_arrival >= date_of_departure:
            return render_template("user/room_details.html", error="Arrival date must be before departure date")

        # Check if the room is available based on its availability
        room = Room.query.get(room_id)
        if room.status != "available":
            return render_template("user/room_details.html", error="Room is not available for booking")

        # Create a new booking record in the database
        booking = Booking(date_of_arrival=date_of_arrival, date_of_departure=date_of_departure, status="pending", room_id=room_id, user_id=session["user_id"])
        db.session.add(booking)
        db.session.commit()

        # Redirect or render a success page
        return redirect(url_for("user.profile_page"))

    return render_template("user/room_details.html")


@room.route("/update-booking-status/<int:booking_id>", methods=["POST"])
def update_booking_status(booking_id):
    new_status = request.json.get("newStatus")

    # Retrieve the booking from the database based on the booking_id
    booking = Booking.query.get(booking_id)

    if booking:
        # Update the status of the booking
        booking.status = new_status

        # Save the changes to the database
        db.session.commit()

        return jsonify({"message": "Booking status updated successfully"})
    else:
        return jsonify({"message": "Booking not found"}, 404)
