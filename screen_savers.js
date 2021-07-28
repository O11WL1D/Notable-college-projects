function zed() {
    pins.analogWritePin(AnalogPin.P0, 0)
    pins.analogWritePin(AnalogPin.P1, 0)
    pins.analogWritePin(AnalogPin.P2, 0)
}



function run() {
    //if hits left wall, : left turns right, right turns left 
    //if hits right wall, left turns right, right turns left
    //if hits floor, down turns up, direction stays
    //if hits ceil, up turns down, direction stays          --essentially invert varible based on wall, if(floor||ceil)(direction=!direction)

    //if hits corner -- reset ball 

    let selection = [-1, 5];
    let x_axis = 3;
    let y_axis = 1;

    //neighboring values of direction indicate left or right
    let direction = true;
    //1=up
    //0=down
    let left_right = false;
    //1=left
    //0=right


    let toggle = x_ARG;
    let rows = [-1, -1, -1, -1, -1];
    //each row value specifys the position of a droplet

    let selecTT;
    let rain_x = 0;
    let rain_y = 0;
    if (toggle == 1) { led.toggle(x_axis, y_axis); }


    let counter = 0;
    let x_x = -1;
    let y_y = 0;

    let rand_x = -2
    let rand_y = -2

    let quad = 3;

    let counterr = 0;
    let led_list = [25]
    let xI = 0;
    let Bree = 1
    let largest = 0;

    let multiple_count = 0;

    //check, then increment. 
    for (; Bree == 1;) {





        if (toggle == 0) {

            basic.pause(100)

            //randomly select row to add rain drops, the outer sides are kept free of rain


            if (y_y == 4) { led.toggle(x_x, y_y); y_y = -1; x_x = Math.randomRange(0, 4); led.toggle(x_x, y_y) }


            led.toggle(x_x, y_y)
            y_y += 1;
            led.toggle(x_x, y_y)








        }






        //--------------------bouncing ball screen saver 
        if (toggle == 1) {






            //console.log("cycle")
            //console.log(""+x_axis);
            //console.log(""+y_axis);


            basic.pause(200)
            if (y_axis == 0) { direction = (!direction) };
            if (y_axis == 4) { direction = (!direction) };

            if (x_axis == 0) { left_right = (!left_right) };
            if (x_axis == 4) { left_right = (!left_right) };

            //upwards left
            if (direction == true && left_right == true) {

                led.toggle(x_axis, y_axis);
                y_axis += 1;
                x_axis -= 1;
                led.toggle(x_axis, y_axis);
                console.log("up_left")
            }

            //upwards right
            if (direction == true && left_right == false) {

                led.toggle(x_axis, y_axis);
                y_axis += 1;
                x_axis += 1;
                led.toggle(x_axis, y_axis);

                console.log("up_right")
            }


            //Downwards left
            if (direction == false && left_right == true) {


                led.toggle(x_axis, y_axis);
                y_axis -= 1;
                x_axis -= 1;
                led.toggle(x_axis, y_axis);

                console.log("down_left")

            }
            //Downwards right
            if (direction == false && left_right == false) {


                led.toggle(x_axis, y_axis);
                y_axis -= 1;
                x_axis += 1;
                led.toggle(x_axis, y_axis);
                console.log("down_right")

            }


            //console.log(""+direction)
            //console.log(""+left_right)

        }



        //--------------------------------------------multiples of screen_saver
        if (toggle == 2) {


            counter += 1

            console.log("-------------Selected number")
            console.log("" + counter)

            for (let g = 1; g < 26; g++) {
                basic.pause(100)

                // go through each led to match corresponding g value.
                if (x_x != 4) { x_x += 1 } else {
                    x_x = 0;

                    if (y_y != 4) { y_y += 1 } else { y_y = 0 }


                }

                //console.log("----------------count----------------")
                //console.log("" + g)

                //console.log("x_val");
                //console.log("" + x_x)
                //console.log("y val")
                //console.log("" + y_y);



                if ((counter % g) > 0) { led.unplot(x_x, y_y) } else { led.plot(x_x, y_y); console.log("multiple"); multiple_count += 1; console.log("" + g); largest = g; };

                //Light up led 0 if currently evaluated number is odd. --must update largest multiple to find current value, which is later analized. 
                //Light up led 1 if currently evaluated number is even.
                //light up led 2 if currently evaluated number is a prime factor. --analog pin 2





            }
            if (largest % 2) { pins.analogWritePin(AnalogPin.P1, 1023); pins.analogWritePin(AnalogPin.P0, 0) } else { pins.analogWritePin(AnalogPin.P1, 0); pins.analogWritePin(AnalogPin.P0, 1023) }
            if (multiple_count > 2) { pins.analogWritePin(AnalogPin.P2, 1023) } else { pins.analogWritePin(AnalogPin.P2, 0) };
			pins.analogWritePin(AnalogPin.P2, 0)
            multiple_count = 0;
            largest = 0;

        }



        //--------------------------------------random line generator screen_saver 
        if (toggle == 3) {


            rand_y = selection[Math.randomRange(0, 1)]
            if (rand_y == -1) { direction = true } else { direction = false }
            rand_x = Math.randomRange(-2, 5)
            left_right = !left_right

            for (let x = 0; x < 2; x++) {

                x_axis = rand_x;
                y_axis = rand_y;


                for (let i = 0; i < 5; i++) {
                    basic.pause(50)








                    //upwards left
                    if (direction == true && left_right == true) {



                        y_axis += 1;
                        x_axis -= 1;
                        led.toggle(x_axis, y_axis);
                        console.log("up_left")
                    }

                    //upwards right
                    if (direction == true && left_right == false) {


                        y_axis += 1;
                        x_axis += 1;
                        led.toggle(x_axis, y_axis);

                        console.log("up_right")
                    }


                    //Downwards left
                    if (direction == false && left_right == true) {



                        y_axis -= 1;
                        x_axis -= 1;
                        led.toggle(x_axis, y_axis);

                        console.log("down_left")

                    }
                    //Downwards right
                    if (direction == false && left_right == false) {



                        y_axis -= 1;
                        x_axis += 1;
                        led.toggle(x_axis, y_axis);
                        console.log("down_right")

                    }
                }











            }


        }



        if (toggle == 4) {


            //basic.pause(100)



            counterr += 1
            //console.log("" + counterr)
            if (counterr == 800) {
                xI += 1; quad = Math.randomRange(1, 4); counterr = 0

                if (quad == 1) { led.unplot(0, 0); led.unplot(1, 0); led.unplot(0, 1); led.unplot(1, 1); led_list[(0 * 5) + 0] = xI; led_list[(0 * 5) + 1] = xI; led_list[(1 * 5) + 0] = xI; led_list[(1 * 5) + 1] = xI; }
                if (quad == 2) { led.unplot(3, 0); led.unplot(4, 0); led.unplot(3, 1); led.unplot(4, 1); led_list[3 + (0 * 5)] = xI; led_list[4 + (0 * 5)] = xI; led_list[3 + (1 * 5)] = xI; led_list[4 + (1 * 5)] = xI; }
                if (quad == 3) { led.unplot(0, 3); led.unplot(1, 3); led.unplot(0, 4); led.unplot(1, 4); led_list[0 + (3 * 5)] = xI; led_list[1 + (3 * 5)] = xI; led_list[0 + (4 * 5)] = xI; led_list[1 + (4 * 5)] = xI; }
                if (quad == 4) { led.unplot(3, 3); led.unplot(4, 3); led.unplot(3, 4); led.unplot(4, 4); led_list[3 + (3 * 5)] = xI; led_list[4 + (3 * 5)] = xI; led_list[3 + (4 * 5)] = xI; led_list[4 + (4 * 5)] = xI; }



            }
            //quad = 4 //Math.randomRange(1, 4); 
            console.log("" + xI)

            x_x = Math.randomRange(0, 4)
            y_y = Math.randomRange(0, 4)
            //console.log("" + led_list[x_ + (y_y * 5)]);
            if (led_list[x_x + (y_y * 5)] != xI) { led.toggle(x_x, y_y) }
        }


        if (x_ARG == 1 || x_ARG == 2 || x_ARG == 3 || x_ARG == 4) {
            input.onGesture(Gesture.Shake, function () {
                //tog1
                x_ARG = 0
                Bree = 0;
                zed();
            })
        }

        if (x_ARG == 0 || x_ARG == 2 || x_ARG == 3 || x_ARG == 4) {

            input.onGesture(Gesture.LogoUp, function () {
                //tog2
                x_ARG = 1
                Bree = 0;
                zed();
            })
        }

        if (x_ARG == 0 || x_ARG == 1 || x_ARG == 3 || x_ARG == 4) {
            input.onGesture(Gesture.TiltLeft, function () {
                //tog3
                x_ARG = 2
                Bree = 0;
                zed();
            })
        }

        if (x_ARG == 0 || x_ARG == 1 || x_ARG == 2 || x_ARG == 4) {
            input.onGesture(Gesture.TiltRight, function () {
                //tog4
                x_ARG = 3
                Bree = 0;
                zed();
            })
        }


        if (x_ARG == 0 || x_ARG == 1 || x_ARG == 2 || x_ARG == 3) {
            input.onGesture(Gesture.LogoDown, function () {
                //tog5
                x_ARG = 4
                Bree = 0;
                zed();
            })
        }







    }






}


















let x_ARG = 0 //is value of screen saver.  
let gesture = 0;
let Apress = 0

for (; ;) {

    input.onButtonPressed(Button.A, function () {
        Apress = 1;
    })
    input.onButtonPressed(Button.B, function () {
        Apress = 0;
    })







    if (Apress == 0) { basic.showString("yeah") }
    if (Apress == 1) { run() }
    basic.clearScreen()
    console.log("iteration")
    console.log("" + x_ARG)

}






