#Access Policy Options and AWS IAM
You can manage access to your Amazon S3 resources using access policy options. By default, all
Amazon S3 resources—buckets, objects, and related subresources—are private: only the resource
owner, an AWS account that created them, can access the resources. The resource owner can then grant
access permissions to others by writing an access policy. Amazon S3 access policy options are broadly
categorized as resource-based policies and user policies. Access policies that are attached to resources
are referred to as resource-based policies. Example resource-based policies include bucket policies and
access control lists (ACLs). Access policies that are attached to users in an account are called user policies.
Typically, a combination of resource-based and user policies are used to manage permissions to S3
buckets, objects, and other resources.
For most data lake environments, we recommend using user policies, so that permissions to access
data assets can also be tied to user roles and permissions for the data processing and analytics services
and tools that your data lake users will use. User policies are associated with AWS Identity and Access
Management (IAM) service, which allows you to securely control access to AWS services and resources.
With IAM, you can create IAM users, groups, and roles in accounts and then attach access policies to them
that grant access to AWS resources, including Amazon S3. The model for user policies is shown in the
following figure. For more details and information on securing Amazon S3 with user policies and AWS
IAM, please reference: Amazon Simple Storage Service Developers Guide and AWS Identity and Access
Management User Guide.

# Links
https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html

https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html
