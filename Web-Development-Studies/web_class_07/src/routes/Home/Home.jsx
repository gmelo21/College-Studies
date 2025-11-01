import { Fade } from 'react-slideshow-image';
import 'react-slideshow-image/dist/styles.css';

export default function Home() {
    const images = [
        "src/assets/img1.jpg",
        "src/assets/img2.jpg",
        "src/assets/img3.jpg",
    ];

    return (
        <div className="flex justify-center">
            <div className="max-w-4xl">
                <Fade scale={0.4}>
                    {images.map((img, index) => (
                        <img
                            key={index}
                            src={img}
                            alt={`Slide ${index + 1}`}
                            style={{
                                width: "100%",
                                height: "auto",
                                objectFit: "cover",
                            }}
                        />
                    ))}
                </Fade>
            </div>
        </div>
    );
}
