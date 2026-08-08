Title: Static Website Hosting using Amazon S3 and CloudFront

This project demonstrates how to host a static website using Amazon S3 and deliver the website through Amazon CloudFront for faster and secure content delivery.

Steps Performed

Created an Amazon S3 bucket to store the website files.

Uploaded website files such as index.html and other assets to the bucket.

Enabled Static Website Hosting in the S3 bucket properties.

Configured a bucket policy to allow public read access to the objects.

Verified the website using the S3 static website endpoint.

Created a CloudFront distribution and configured the S3 bucket as the origin.

Accessed the website through the CloudFront distribution URL.

Access Links

CloudFront URL:
https://dksacoc9hek46.cloudfront.net/

S3 Website Endpoint:
http://123456789-sak.s3-website.us-east-1.amazonaws.com/

Direct S3 Object URL:
https://123456789-sak.s3.amazonaws.com/index.html

Conclusion

The website is successfully hosted using Amazon S3 and delivered globally using CloudFront. CloudFront improves performance by caching the content at edge locations and providing faster access to users.