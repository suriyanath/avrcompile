
public class Multipart {
    public static void main(String[] args) {
        //System.out.println("hello");
         HttpClient httpclient = new DefaultHttpClient();
         HttpPost httpPost = new HttpGet("http://localhost:5000/");

         //FileBody uploadFilePart = new FileBody(uploadFile);
         //MultipartEntity reqEntity = new MultipartEntity();
         //reqEntity.addPart("upload-file", uploadFilePart);
         //httpPost.setEntity(reqEntity);

         HttpResponse response = httpclient.execute(httpPost);
         
    }
}

