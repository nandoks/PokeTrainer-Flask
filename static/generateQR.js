function generateQR(code) {
			elem = 'qr'.concat(code)
			var qr = document.getElementById(elem);
			console.log(elem)
			console.log(qr)
			
			// var trainercode = document.createElement("p");
			// trainercode.id = "trainer-code"
			// trainercode.classList.add = "trainer-code"
			// trainercode.innerHTML = code

			// divcode.appendChild(qr)
			// divcode.appendChild(trainercode)

			var qrcode = new QRCode(qr);
			
			qrcode.makeCode(code);

		}