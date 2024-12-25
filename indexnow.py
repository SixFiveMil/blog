import os
import requests
import uuid
import logging
from typing import List, Optional

class IndexNowSubmitter:
    def __init__(self, domain: str, api_key: Optional[str] = None):
        """
        Initialize IndexNow submitter
        
        :param domain: Your website's domain
        :param api_key: Optional custom API key (generates if not provided)
        """
        self.domain = domain
        self.api_key = api_key or str(uuid.uuid4())
        self.endpoint = "https://api.indexnow.org/indexnow"
        
        # Configure logging
        logging.basicConfig(
            level=logging.INFO, 
            format='%(asctime)s - IndexNow - %(levelname)s: %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def submit_urls(self, urls: List[str]) -> bool:
        """
        Submit URLs to IndexNow participating search engines
        
        :param urls: List of URLs to submit
        :return: Submission success status
        """
        payload = {
            "host": self.domain,
            "key": self.api_key,
            "urlList": urls
        }

        try:
            response = requests.post(
                self.endpoint, 
                json=payload, 
                timeout=10
            )
            
            if response.status_code == 200:
                self.logger.info(f"Successfully submitted {len(urls)} URLs")
                return True
            else:
                self.logger.error(f"Submission failed: {response.status_code}")
                return False
        
        except requests.RequestException as e:
            self.logger.error(f"Network error: {e}")
            return False

    def submit_sitemap(self, sitemap_path: str) -> int:
        """
        Extract and submit URLs from a sitemap
        
        :param sitemap_path: Path to XML sitemap
        :return: Number of URLs submitted
        """
        import xml.etree.ElementTree as ET
        
        try:
            tree = ET.parse(sitemap_path)
            root = tree.getroot()
            
            # Namespace handling for sitemaps
            namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            
            urls = [
                url.find('ns:loc', namespace).text 
                for url in root.findall('.//ns:url', namespace)
            ]
            
            self.submit_urls(urls)
            return len(urls)
        
        except Exception as e:
            self.logger.error(f"Sitemap processing error: {e}")
            return 0

def main():
    # Example usage
    indexer = IndexNowSubmitter(
        domain="codeandcypher.com", 
        api_key="0715c989f03a42fe9ef4c02db06ae8e9"
    )
    
    # Submit individual URLs
    #new_urls = [
    #    "https://example.com/new-blog-post",
    #    "https://example.com/updated-page"
    #]
    #indexer.submit_urls(new_urls)
    
    # Submit from sitemap
    indexer.submit_sitemap(r"C:\Users\joshu\Documents\codeandcypher\public\sitemap.xml")

if __name__ == "__main__":
    main()