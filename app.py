import asyncio
from playwright.async_api import async_playwright

async def get_delhi_clients():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # Set headless=False to see the browser
        page = await browser.new_page()
        await page.goto("https://www.justdial.com/Delhi/Web-Designing-Services/nct-10589480")

        await page.wait_for_selector(".cntanr")  # Wait until content is loaded

        companies = []
        items = await page.query_selector_all(".cntanr")
        for item in items:
            name_el = await item.query_selector(".lng_cont_name")
            phone_el = await item.query_selector(".contact-info")
            address_el = await item.query_selector(".cont_sw_addr")

            name = await name_el.inner_text() if name_el else "N/A"
            phone = await phone_el.inner_text() if phone_el else "N/A"
            address = await address_el.inner_text() if address_el else "N/A"

            companies.append({
                "Name": name.strip(),
                "Phone": phone.strip(),
                "Address": address.strip()
            })

        await browser.close()
        return companies

# Run the async function
if __name__ == "__main__":
    import pprint
    result = asyncio.run(get_delhi_clients())
    pprint.pprint(result)
