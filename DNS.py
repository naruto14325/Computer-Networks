# dns_resolver.py
import dns.resolver
import logging

# Configure logging to a file
logging.basicConfig(filename="dns_results.txt",
                    level=logging.INFO,
                    format="%(asctime)s - %(message)s")

def query_dns(domain):
    record_types = ["A", "MX", "CNAME"]

    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(domain, rtype, raise_on_no_answer=False)
            if answers.rrset:
                print(f"\n=== {rtype} Records for {domain} ===")
                for r in answers:
                    print(r.to_text())
                    logging.info("%s record for %s: %s", rtype, domain, r.to_text())
            else:
                print(f"\nNo {rtype} records found for {domain}")
                logging.info("No %s records for %s", rtype, domain)
        except Exception as e:
            print(f"\nError retrieving {rtype} record for {domain}: {e}")
            logging.error("Error retrieving %s record for %s: %s", rtype, domain, e)

if __name__ == "__main__":
    domain = input("Enter a domain name (e.g., example.com): ").strip()
    query_dns(domain)
    print("\nResults have also been logged to dns_results.txt")

