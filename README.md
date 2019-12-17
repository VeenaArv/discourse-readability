# discourse-readability
Using discourse features to predict readability of text 

## Data collection
### High quality examples 
1. Simple Wiki
    * [Very good simple wikipedia articles](https://simple.wikipedia.org/wiki/Wikipedia:Very_good_articles/by_date)
    * [Good simple wikipedia articles](https://simple.wikipedia.org/wiki/Category:Good_articles) 
2. Regular Wiki
    * [Good wikipedia articles](https://en.wikipedia.org/wiki/Wikipedia:Good_articles/all)
    * [Featured wikipedia articles](https://en.wikipedia.org/wiki/Wikipedia:Featured_articles)
    * [Technical wikipedia articles](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_that_are_too_technical_from_March_2014)

## Penn Discourse Treebank (PDTB) Discourse Parser

### Source
Ziheng Lin, Hwee Tou Ng and Min-Yen Kan (2014). A PDTB-Styled End-to-End Discourse Parser. Natural Language Engineering, 20, pp 151-184. Cambridge University Press.

[Java implementation](https://github.com/WING-NUS/pdtb-parser) (Developed and maintained by Ilija)

### Usage

To run on wiki pages:
```
java -jar parser.jar ../discourse-readability/data/curated_data/
```
## Discourse Features

Currently only uses number of implicit and explicit discourse relations in a single page