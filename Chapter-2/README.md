# Chapter-2 Digital Images Format 

## 2.1 - Elements of Visual Perception

<hr>
28-01-2022 

### The Structure of the eye 
The eye is really a wonder of nature, so perfect it works, and I am going to start my new journey studying a bit about this beautiful machine. How humans percieve
vision is of a great interest to us. The human eye has 3 membrane structure, one of them is retina, which forms the part of the eye where the images are 
formed inside the eye. It percieves this image and sends the signal to the brain (how brilliant). 

The light perception happens in the **retina** region of the eye. which lines the inside walls of the poserior region. It has two types of receptors, cones and rods. It's also very interesting to see how these two acts as two dfferent types of receptors. 

 **Cones**
- There are about 6-7 million in numbers, mostly located in the central region of the retina (known as Fovea, also check the diagram below)/
- They are highly sensitive to the color. 
- Each cone is connected to a nerve end and hence they can resolve fine details of the scene. 
- Cone Vision is known as <i>photopic</i> or <i>bright light vision</i>.

**Rods**
- There are about 75 to 150 million rods present in each eye (yes, much much larger)
- They don;t have a separate nerve ending for each cell and several rods are connected to a single nerve ending, th is reduces the information that is carried forward and hence rods capture the overall image of the field of view. 
- They are not involved in color visoin and are sensitive to low levels of illumination. 
- Rods vision is known as <i>scotopic </i> or <i>dim-light </i>

"Objects that appear colored during the day, appear as colorless forms in the moonlight" and now you know why, because for the latter, only the rods are stimulated. 

Also, what I refer to it as, that rods and cones capture different qualities of the scene, cones is much more interested in capturing the color, brighness and hue of the scene, where rods capture the shapes, distance and other basic characterisitics of the scene. 


**Figure 2.2**
<br>
![](images/figure_2_2.jpeg)

The above figure shows the density of cones and rods in the cross-section of the right eye. 
- The disitribution is almost symmetrical about Fovea (present at 0 degrees), but there is a point at around 20 degrees (left of Fovea in the figure) called the blind spot. This is the region where optic nerve is connected to the eye and hence, no receptors are present at this region. 
- The Fovea here represents a circular region in the retina and has an area of about 1.7 mm squares. 
- Cones are mostly located in the center area of fovea. 
- Rode are more uniformly located then cones, their density increases in density from center out to approximately <img src="https://latex.codecogs.com/svg.image?20^{\circ}" title="20^{\circ}" /> off axis. Then, their density decreases out to the periphery of the retina.

One interesting thing to note here is that the fovea contains about 265,000 cones. So, this much amount of ligh sensors. It's many isn't. But here comes the interesting thing, **Most electronic imaging chips exceed this number by a large factor**.

<hr>
09-02-2022 

### Image Formation in the eye 
- There's a difference between how an ordinary photographic camera focusses on object to how an human eye would do it. 
- In case of a camera, the lens has a fixed focal lenght and the image is formed on the film (imaging chip, or retina of the camera) by varying the distance between the lens and the film. 
- However in the case of human eye, this distance is fixed (between the lens and retina). In this case, the image is formed on the retina by chanding the shape and hence the focal length of the lens is adjusted such that image is formed on the retian. 
- And this happens so effortlessly. If you are seeing the screen right now, and just look at the background (wall or whatever) then the eye will automatically change the focal length of the eye such that the image is formed on the back of retina, isn't brilliant, how efforotlessly it happens. 
- The next cool thing is that we can also find the length of the image formed inside the retina. 

![Figure 2.3](images/figure_2_3.jpeg)

One can even try it practically, if you know the length of the screen in front of you and also the distance of the screen from the eyes, then using hte formulae in the above image we can calculate the length of the intverted image formed in the retina. 


### Brightness Adaptation and Discrimation

Whenever we go to movies, and enter the theater, it takes some time for the eyes to adjust and before that everything appears very dark. But after some time, we are able to see the different compoenents inside the theater, like the stairs and the curtains, which was not visible before. This is the phenomenon we are going to study in this section. 

The human eye can adapt to a large intensity levels, from the scotopic limit to the glare limit. 

As we have seen in the previous section that vision perception is done through cones and rods and the type of vision is named as photopic and scotopic vision respectively. 

In the graph below, we can see that there is a logarithmic relationship between the subjective brightness (intensity as percieved as the human visual system) and light intensity incident on the eye. 

![Figure 2.4](images/figure_2_4.jpeg)

The question arises that if our eyes are able to adjust to such vast range of intensities, why do we have that phenonmenon discussed at the starting of this section. The answer to this the eyes cannot operate on such a vast range **simontaneously**. It accomplished this variation by changing it's overall sensitivity, a phenomenon known as **brightness adjustment**. 

So, the big fat line that is given in the graph, this variation of intensities can't be seen simontaneously by our human eye. But if one looks at the another line given in the graph, at brightness level <img src="https://latex.codecogs.com/svg.image?B_{a}" title="B_{a}" />, this represents the range of brightness that our eyes can see simontaneously. 

At a given intensity range, the current sensitivity level of the visual system is called the brightnesss adaptaion level. When the brightness adaptation level is <img src="https://latex.codecogs.com/svg.image?B_{a}" title="B_{a}" /> the eye can adjust to the brightness represented by the given intersecting curve (which is small comapred to the overall range). 

At this level, the eyes can percieve brighntess as low as <img src="https://latex.codecogs.com/svg.image?B_{a}" title="B_{b}" />, below then that everything would be black. Now we know what was happening when we entered the theater. 

This brightness adaptaion level keeps on changing and our eyes keeps adjusting and the life goes on !! 

<hr>
21-02-2022 

### Brightness Discrimination 

- **Defination**
Brightness Discrimation means the ability to discriminate between changes in light intensity at a specific apaptation level. 

- **Experiment** 
A classical experiement to study brightness discrimination is done by placing a large opaque glass, large enough to fill the whole of occupy the entire field of view. This opaque glass has an intensity <img src="https://latex.codecogs.com/svg.image?I" title="I" /> (which is variable). 

In the center of this field, a flash of intensity <img src="https://latex.codecogs.com/svg.image?I&space;&plus;&space;\Delta&space;I&space;" title="I + \Delta I " /> is flashed out in the form of a circle. 

Now, our main interest lies at what value of <img src="https://latex.codecogs.com/svg.image?\Delta&space;I&space;" title="\Delta I " /> is a human able to differentiate the change. 

The ratio <img src="https://latex.codecogs.com/svg.image?\frac{\Delta&space;I_{c}}{I}&space;" title="\frac{\Delta I_{c}}{I} " />, where <img src="https://latex.codecogs.com/svg.image?\Delta&space;I_{c}" title="\Delta I_{c}" /> is increment of illumination discriminable 50% of the time with background illumination I, is called **Weber Ratio**. 

If the weber ratio is **high**, it means that a large change is required for the change to be percievable, which means that the Brightness Discrimation is **poor** , on the other hand, if weber ratio is **low**, this means that a small change in illumination is required for that given intensity, for a change to be percievable, and hence Brightness Discrimination is **good**. 

- **Plot of weber ratio with given Intensity level** 

(to be completed) 

<hr> 
05-03-2022 

## Light and the Electromagnetic Spectrum

### Electromagnetic Spectrum
EM spectrum refers to the distribution of waves, wrt to wavelength or frequency. A wave can be represented by Wavelength and frequency, which are related by 

<img src="http://latex.codecogs.com/svg.latex?\lambda&space;=&space;\frac{c}{\nu&space;}" title="http://latex.codecogs.com/svg.latex?\lambda = \frac{c}{\nu }" />, where c is the speed of light. 

Energy of a component of EM spectrum with a frequency <img src="http://latex.codecogs.com/svg.latex?\nu" title="http://latex.codecogs.com/svg.latex?\nu" /> is given by - 

<img src="http://latex.codecogs.com/svg.latex?E&space;=&space;h\nu" title="http://latex.codecogs.com/svg.latex?E = h\nu" />, where h is plank's constant. 

- Waves having more frequency (lower wavelength) have more energy. 
- In the EM spectrum, gamma rays have the most energy followed by X-rays, where radio waves have the lowest energy. 

### More about the visible band 
Light is a type of EM spectrum which can be detected by the eye, this falls under the range of 0.43 <img src="http://latex.codecogs.com/svg.latex?\mu&space;m" title="http://latex.codecogs.com/svg.latex?\mu m" /> to 0.79 <img src="http://latex.codecogs.com/svg.latex?\mu&space;m" title="http://latex.codecogs.com/svg.latex?\mu m" />

- The sequenece of colors in the Visible band are as follows - Violet, Blue, Green, Yellow, Orange and Red. Although these colors don't end aburuptly, it's a continous change and one color bends smooothly into the next. 

### How Colors are percieved 
- The color percieved by us in an object is defined by the nature of light reflected by the object. 
- An object appearing Green will reflect the waves with wavelengths in the range of green color, while absorbing the rest. An objcet appearing white would absorb / reflect each color in (almost) same propotion. 

### Achromatic and Chromatic Light
- Light that is void of a color is known as monochromatic ( achhromatic light), it can be characterized by intensity, which is also known as gray-level
- Unlike achromatic light, chromatic light contains color. It is characterized by Radiance, Luminance and brightness. 

### Generating Images in other bands 
As discussed earlier, human eyes can only see the electromagnetic waves which fall in the region of Visible Range. But, can we "see" waves belonging to the rest of the spectrum? 

In principle, if we can develop a sensor that is capable of detecting energy radiated in a band of the electromagnetic spectrum, we can image the events interest in that band. So, we can have specific sensor, for example, to capture x-rays, then we can "see" X-rays as well. (Not from the naked eye though).


<hr> 
25-03-2022 

## Image Aquisition 

### How are Images formed 

There are two main components associated with formation of images, one is illumniation of the ligth from the source, now this source is not just limited to visible light, but it can be anything like X-rays, or Infrared rays. The second component is refelction or absorption (transmission through) of the energy from the source by the objects. Examples for reflection and transmission through are images formed by visible rays, and x-rays respectively. 

### Using Single Sensing element to convert energy into digital images
Energy once gathered is then converted to Digital signals using single sensing element (shown in the figure). 

The single sensing element contains a Sensing Material that is response to the type of energy being detected. A filter is used to filter out the incident enegy for selectivity. The output of a Sensing Material is a voltage proportional to the energy intensity. 

The Single Sensing Element can be used in different combinations to acquire images - 

![](images/figure_2_13_1.jpeg)

- ### Using one Single Sensing Element 
  In this case, there has a be a relative displacement between the x and y directions between the sensor and area to be imaged, a sample architecture for it is displayed in the figure below. 
  
![](images/figure_2_13_3.jpeg)
  
- ### Using Sensor Strips 
  A sensor strip is a linear combination of Single Sensing Elements. In this case we only require the movement between the sensor and area to be imaged only in one direction. 
  
  A more popular use of Sensor strips is using it in a ring formations which is also used in many medical use cases like MRI and PET. This can be seen in the figure below. 
  ![](images/figure_2_14.jpeg)

  
- ### Using Image Arrays 
  In this case, we are using a 2-D array of Single Sensing Elements, and this is the method used in digital cameras. No motion is required in this case. 
  
  ![](images/figure_2_15.jpeg)


<hr> 
07-04-2022 

### Sample Image Formation Model 

Mathematically, images can be represented as a two-dimensional function, f(x,y). Where f is a scalar quantity for a given spatial coordinate (x,y). Further f(x,y) can be represented as a product of i(x,y) and r(x,y), where i and r are the amount of illumination incident from the source, and the amount of illumination reflected (or transmitted) by the object in the scene. And this is how Images can be represented mathematically. 

<hr> 
23-04-2022 

## Image Sampling and Quantization 
As we saw in the last topic, an image can be represented as a function f(x,y), where (x,y) are spatial coordinates and f is the intensity levels at (x,y). Now furthur, images can be of two types classified on the basis on what the values x,y and f corresponds to. An image can either be 
1. Analog Image 
2. Digital Image 

In Analog image the values x,y and f are continous, and in digital images these values are discrete. To convert an image from analog to digital, we require the two processed of Sampling and Quanitzation. 

### Sampling 
Sampling refers to the process of dividing continous image into x,y coordinates. The method of sampling is determined by the sensor arrangement used to generate the image. This converts the continous image into grid like structure, where each component is called as pixel, and is the basic component of an image. 

### Quanitzation 
Quantization refers to the process of digitizing the amplitude values. In this step, each pixel is assigned a discrete intensity level. Before applying the process of Quantization, amplitude could belong to any value in a continous range, but after this, there are only discrete values to which it can belong. 

- Representing Sampling and Quantization Mathematically - 

![](https://latex.codecogs.com/svg.image?f(x,y)) is a digital image if ![](https://latex.codecogs.com/svg.image?(x,y)&space;) are integers from ![](https://latex.codecogs.com/svg.image?Z^2) and f is a function which assigns an intensity value to each distinct pair of coordinates (x,y). This functional assignment is the quantization. 

<hr> 
26-04-2022

## Representaion of Digital Images 

As we have seen in previous topics that images can be represented as f(x,y). There are 3 methods to represent this - 
- Representing as 3d plot: The first method is to represent it as a 3-d figure with the x,y coordinates being the (x,y) value, and z coordinate representing the value of f. This is mostly used for gray scale images. 
- Representing as it would appear in a Computer Screen or photograph: This is the most comomon used format this method can also be used for color images. 
- Representing as matrices: This representation uses the mathematical values of the image, and is used for computer processing. 

I also made a mini project on this, [Gray Scale Images in 3d](https://github.com/hardikkamboj/GrayImages-in-3d)
