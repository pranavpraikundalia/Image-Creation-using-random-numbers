# Image-Creation-using-random-numbers
This code gets truly random numbers through an HTTP API request from Random.org and then creates a 128x128 size image and displays it.

We have a quota of 2,00,000 free bits from Random.org every day upto 1,000,000 bits and this code acquires more than that. So, either we can buy more bit quota or use limited bits in a different way.

For e.g.
1) Change the max integer value ffrom the http request to make it small and get small integers.(This will reduce the value of RGB and then your image will be black).
2) Use some numbers repeatedly to form a 128x128 matrix.

The code works if you want to test it for a different size of image change the size to a lower value and zoom into to image to check.
