
# Face Anonymization

Crop recommendation is one of the most important aspects of precision agriculture. Crop recommendations are based on a number of factors. Precision agriculture seeks to define these criteria on a site-by-site basis in order to address crop selection issues. While the "site-specific" methodology has improved performance, there is still a need to monitor the systems' outcomes.Precision agriculture systems aren't all created equal. However, in agriculture, it is critical that the recommendations made are correct and precise, as errors can result in significant material and capital loss.


<p align="center">
<img src="https://www.nhbr.com/content/uploads/2021/03/facial-recognition-tech.jpg" height=500 />
</p>
This application will assist farmers in increasing agricultural productivity, preventing soil degradation in cultivated land, reducing chemical use in crop production, and maximizing water resource efficiency.

# [Dataset]()
This dataset was build by augmenting datasets of rainfall, climate and fertilizer data available for India.

### [Attributes information:]()

* **N** - Ratio of Nitrogen content in soil
* **P** - Ratio of Phosphorous content in soil
* **K** - Ratio of Potassium content in soil
* **Temperature** -  temperature in degree Celsius
* **Humidity** - relative humidity in %
* **ph** - ph value of the soil
* **Rainfall** - rainfall in mm 

### [Experiment Results:]()
* **Data Analysis**
    * All columns contain outliers except for N.
 * **Performance Evaluation**
    * Splitting the dataset by 80 % for training set and 20 % validation set.
 * **Training and Validation**
    * GausianNB gets a higher accuracy score than other classification models.
    * GaussianNB ( 99 % accuracy score )
 * **Performance Results**
    * Training Score: 99.5%
    * Validation Score: 99.3%

 
# Demo
Live Demo: https://ai-crop-recommender.herokuapp.com/

![](https://i.imgur.com/TnsSPQy.png)

# References
* https://www.pyimagesearch.com/2020/04/06/blur-and-anonymize-faces-with-opencv-and-python/
* https://deepomatic.com/en/data-anonymization-a-challenge-to-face
* https://arxiv.org/pdf/1803.11556.pdf
* https://hal.archives-ouvertes.fr/hal-01367565/document
* https://towardsdatascience.com/how-to-beat-facial-recognition-systems-with-face-anonymization-6f078179ac82
* https://www.lse.ac.uk/library/research-support/research-data-management/anonymisation-and-data-protection
* https://www.researchgate.net/publication/263506756_Making_Big_Data_Privacy_and_Anonymization_Work_Together_in_the_Enterprise_Experiences_and_Issues
* https://hal.archives-ouvertes.fr/hal-01367565/document
* https://ieeexplore.ieee.org/document/6657284
