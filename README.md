# Review Helpfulness
This is a NLP based project associated to identifying the helpfulness of a product review using Amazon data

## Data
The data was retrieved from the following souruce : https://nijianmo.github.io/amazon/index.html    

## Data Overview  
**VG Reviews Data**  
- reviewerID - ID of the reviewer, e.g. A2SUAM1J3GNN3B  
- asin - ID of the product, e.g. 0000013714   
- reviewerName - name of the reviewer  
- vote - helpful votes of the review  
- style - a disctionary of the product metadata, e.g., "Format" is "Hardcover"  
- reviewText - text of the review  
- overall - rating of the product  
- summary - summary of the review   
- unixReviewTime - time of the review (unix time)    
- reviewTime - time of the review (raw)  
- image - images that users post after they have received the product  

**VG Meta**  
- asin - ID of the product, e.g. 0000031852  
- title - name of the product  
- feature - bullet-point format features of the product  
- description - description of the product    
- price - price in US dollars (at time of crawl)  
- image - url of the product image  
- also_view - other similar products viewed  
- also_buy - other similar products bought  
- salesRank - sales rank information    
- brand - brand name    
- similar_item - list of similar items  
- categories - list of categories the product belongs to  
- tech1 - the first technical detail table of the product  
- tech2 - the second technical detail table of the product  
- similar - similar product table  